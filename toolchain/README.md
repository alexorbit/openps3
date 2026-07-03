# OpenPS3 Toolchain

Tools for analyzing and patching PS3 firmware (OFW 4.93).

## Scripts

### `pup_extract.py`
Extract segments from a PS3Update PUP file.

```
python3 pup_extract.py PS3UPDAT_4.93.PUP [output_dir]
```

Segments extracted include: `version.txt`, `ps3swu.self`, `vsh.tar`, `update_files.tar` (which contains CORE_OS_PACKAGE.pkg), and more.

### `self_extract.py`
Extract the embedded ELF from a SELF (PS3 Signed ELF) file.

**Note:** The SELF must already be decrypted using `unself` from the fail0verflow PS3 tools. This script simply locates and extracts the ELF header and sections from the decrypted SELF.

```
python3 self_extract.py <decrypted.self> [output.elf]
```

### `ps3_disasm.py`
Disassemble a PPC64 ELF using Capstone.

Supports PowerPC64 BE (machine type 21) and PowerPC32 BE (machine type 20). Scans all executable LOAD segments and writes Capstone disassembly to a text file.

```
python3 ps3_disasm.py <elf_file> [output.txt] [--count N]
```

### `patch_lv2.py`
Patch LV2 kernel (decrypted ELF) to skip the LV1 HV call for boot device query.

**Target:** OFW 4.93 `lv2_kernel.self`

**What it does:** Replaces the `sc 1` (HV call) instruction in `sys_ss_get_boot_device`
(syscall 872) with a hardcoded return value, bypassing the need to query
the boot device from LV1. Both code paths are patched:
- `sys/flash/boot` path (returns 8-byte device ID)
- `ss/param/analog` path (returns 1-byte value)

The current patch hardcodes device ID `0x190` (NAND flash).

```
python3 patch_lv2.py lv2_decrypted.elf [patched_lv2.elf]
```

## Requirements

- Python 3.12+
- Capstone (`pip install capstone`)
- fail0verflow PS3 tools (`unpkg`, `cosunpkg`, `unself`) for initial decryption
- RPCS3 `key_vault.cpp` keys (for SCE PKG/SELF decryption)

## Usage Workflow

1. Download OFW PUP from Sony
2. `pup_extract.py PS3UPDAT_4.93.PUP firmware/`
3. Extract and decrypt CORE_OS_PACKAGE.pkg (via unpkg + RPCS3 keys)
4. Decrypt LV2 SELF via `unself`
5. `patch_lv2.py lv2_kernel.elf` to produce patched kernel
6. Disassemble with `ps3_disasm.py` for analysis

## License

Apache-2.0
