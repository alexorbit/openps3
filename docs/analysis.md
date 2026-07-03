# PS3 Firmware Analysis (OFW 4.93)

## Boot Chain

```
BootROM -> metldr -> lv0 -> lv1.self -> lv2_kernel.self -> vsh.self
```

- `appldr` is absent since FW 3.56+ (merged into lv0)
- LV0 entry: `0xC60`
- LV1 entry: `0x3B1390` (function descriptor) -> code at `0x100` -> init at `0x3AF030`
- LV2 entry: `0x8000000000000100` (real-mode address)

## LV1 Architecture

### Sections (decrypted ELF, 4.1 MB, 18 sections)

| Address      | Size     | Flags | Content                        |
|-------------|----------|-------|--------------------------------|
| 0x000200000 | 0x11d8b4 | AW    | Writable data                  |
| 0x0031d8c0 | 0xc320   | AW    | Device path string table       |
| 0x00329be0 | 0x28458  | AX    | Function descriptor table      |
| 0x00352040 | 0x80c0   | AX    | GOT/data                       |
| 0x0035a100 | 0x9c80   | AX    | GOT/data                       |
| 0x00400000 | 0x200000 | AX    | **Main code section**          |
| 0x00600000 | 0x1050   | AX    | Boot code                      |

### Key Structures

**TOC Base:** `0x35A038` (set during init at `0x3AF07C`, stored in `r2`)

**SC (Supervisor Call) Handler:** vaddr `0xC00`
- Dispatch via 8-byte function pointer table at `per_thread_data - 0x6fc8`
- Setup at `0xC30` loads table pointer
- Dispatch at `0xF60` uses `ldx r11, r11, r12` + `bctrl`

**Function Descriptor Table:** vaddr `0x329BE0`, 6873 entries (24 bytes each)
- Each entry: `{code_ptr, toc_ptr, env_ptr}` (toc always `0x35A038`)
- Entries 0-5 are C++ vtable dispatch stubs, NOT indexed by HV call number

**Device Path String Table:** vaddr `0x31DA60`
Contains dotted-path strings separated by `0x5C` (backslash) bytes:
- `sys.flash.boot` / `sys.flash.ext` / `sys.flash.data`
- `sys.param.load.rom1st`
- `lv1.maxplgid`
- `sys.debug*` variants
- `boot.gos.*`
These strings are **not referenced by absolute vaddr** in code — they are
initial values in writable data structures overwritten at boot time.

**Security Subsystem:**
LV1 delegates security operations (signature verification, hash checking) to
embedded FSELFs (`ss_init.fself`, `ss_server*.fself`) inside its data section.
These are encrypted and run on the security co-processor/SPU.
Key C++ classes observed in debug strings:
- `certified_file` / `certified_file_verifier` — handles SELF certification
- `self64_file` — 64-bit SELF handling
- `verify_util` — hash/certificate verification
- `update_manager` / `check_core_os_hash` — integrity checking

### LV2 Loading Function

Found at `0x5CE670`–`0x5CEA00` range (code section 0x400000).
- Reads `lv2_kernel.self` from storage
- Delegates signature verification to security subsystem
- On success: prints `"lv2 called"` and jumps to LV2 entry
- On failure: prints `"lv2 fail :%d"` and halts

Key strings located:
- `"lv2_kernel.self"` at `0x535538`
- `"load_lv2: filename: %s"` at `0x5CE890`
- `"lv2 called"` at `0x5CE992`
- `"lv2 fail :%d"` at `0x5CE9AA`
- `"self64_file: validation of certified_file failed (%d)"` at `0x325F20`

## LV2 Architecture

### Section (decrypted ELF, 3.6 MB)

| Address                 | Size     | Flags | Content                |
|------------------------|----------|-------|------------------------|
| 0x8000000000000000+    | ~3.6 MB  | AX    | Kernel code + data     |

Uses real-mode addresses with `0x8000000000000000` prefix.

### Syscall Dispatch Table

At vaddr `0x8000000000363BF8` — 8-byte entries indexed by syscall number.

### Key Syscall: `sys_ss_get_boot_device` (#872)

**vaddr:** `0x80000000002265CC`

Constructs path components from register immediates and calls LV1 HV call
`0x5B` (91) to resolve a storage device path to a device node ID.

**Path 1 — `sys/flash/boot`:**
- Sets `r4="sys"`, `r5="flash"`, `r6="boot"`, `r7=0`
- Calls `li r11, 0x5B` + `sc 1` (HV call 0x5B)
- Returns 8-byte device ID via `copy_to_user`
- Device ID `0x190` = NAND flash

**Path 2 — `ss/param/analog/sunt`:**
- Sets `r4="ss"`, `r5="param"`, `r6="analog"`, `r7="sunt"`
- Same HV call `0x5B`
- Returns 1-byte value (different query)

### Patch Points

| Location           | vaddr                          | Original          | Patched           |
|--------------------|--------------------------------|--------------------|--------------------|
| Path 1 `li r11`   | `0x8000000000226674`           | `li r11, 0x5b`    | `li r3, 0`        |
| Path 1 `sc 1`     | `0x8000000000226678`           | `sc 1`            | `li r30, 0x190`   |
| Path 1 rest       | `0x22667C`–`0x226684`         | `cmpdi/bne/mr`    | `nop`×3           |
| Path 2 `li r11`   | `0x8000000000226768`           | `li r11, 0x5b`    | `li r3, 0`        |
| Path 2 `sc 1`     | `0x800000000022676C`           | `sc 1`            | `li r30, 0x190`   |
| Path 2 rest       | `0x226770`–`0x226778`         | `cmpdi/bne/mr`    | `nop`×3           |

## Signature Verification Architecture

LV2 signature verification flows:
1. LV1 reads `lv2_kernel.self` from boot device
2. LV1 parses the SELF using `self64_file` class
3. LV1 sends the SELF content to the security co-processor via SPU modules
   (`certified_file_verifier` uses SIGSPU* messages)
4. Security co-processor validates the certificate chain against hardware root key
5. Result checked via status register / callback
6. On failure: `"lv2 fail :%d"` printed, system halts

**Bypass strategy:** Locate the `cmpwi`/`bne` (or equivalent) in LV1 code
that checks the verification result and NOP the conditional branch.

## Key Observations

- String addresses in LV1/LV2 are **never referenced by absolute vaddr in code**
  — they exist as initial values in writable data structures or GOT entries
- The function descriptor table at `0x329BE0` is for C++ vtable dispatch,
  not HV call dispatch
- Security-sensitive operations are delegated to encrypted embedded FSELFs
  (cannot be directly analyzed from the decrypted LV1 ELF)
- GOT entries for string pointers exist in section 7 (vaddr `0x352040`)
  (e.g., self64_file failure string at GOT `0x3571E8`)

## Tools

See [toolchain README](../toolchain/README.md) for usage.

- `toolchain/pup_extract.py` — Extract PUP segments
- `toolchain/self_extract.py` — Extract ELF from decrypted SELF
- `toolchain/ps3_disasm.py` — Disassemble PPC64 ELF with Capstone
- `toolchain/patch_lv2.py` — Patch LV2 kernel (boot device HV call bypass)

## Legal

This document contains factual findings and observations from reverse engineering
the PS3 OFW 4.93 firmware. No copyrighted Sony code is included. Toolchain scripts
are original work (MIT licensed).
