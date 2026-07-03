#!/usr/bin/env python3
"""
Patch LV2 kernel (decrypted ELF) to skip HV call 0x5B for boot device query.

Target: OFW 4.93 lv2_kernel.self (syscall 872: sys_ss_get_boot_device)

HV call 0x5B resolves a device path (e.g., "sys.flash.boot") to a device node ID.
This patch replaces both call sites with hardcoded return values, bypassing
the LV1 call entirely.

Usage:
    python3 patch_lv2.py lv2_decrypted.elf [patched_output.elf]
"""

import struct
import sys
import os


def read_elf(elf_path):
    with open(elf_path, 'rb') as f:
        return f.read()


def write_elf(elf_path, data):
    with open(elf_path, 'wb') as f:
        f.write(data)


def get_segment_info(data):
    e_phoff = struct.unpack('>Q', data[0x20:0x28])[0]
    e_phentsize = struct.unpack('>H', data[0x36:0x38])[0]
    e_phnum = struct.unpack('>H', data[0x38:0x3A])[0]

    segments = []
    for i in range(e_phnum):
        off = e_phoff + i * e_phentsize
        p_type = struct.unpack('>I', data[off:off+4])[0]
        p_vaddr = struct.unpack('>Q', data[off+16:off+24])[0]
        p_offset = struct.unpack('>Q', data[off+8:off+16])[0]
        p_filesz = struct.unpack('>Q', data[off+32:off+40])[0]
        p_flags = struct.unpack('>I', data[off+4:off+8])[0]
        segments.append({'type': p_type, 'vaddr': p_vaddr, 'offset': p_offset,
                         'filesz': p_filesz, 'flags': p_flags})
    return segments


def vaddr_to_offset(data, vaddr):
    segs = get_segment_info(data)
    for s in segs:
        if s['type'] == 1 and s['vaddr'] <= vaddr < s['vaddr'] + s['filesz']:
            return s['offset'] + (vaddr - s['vaddr'])
    return None


def write_word(data, vaddr, word32):
    off = vaddr_to_offset(data, vaddr)
    if off is None:
        print(f'ERROR: vaddr 0x{vaddr:x} not found in any segment')
        return False
    data = bytearray(data)
    struct.pack_into('>I', data, off, word32)
    return bytes(data)


def patch_hv_call(data, device_id=0x190):
    """
    Patch sys_ss_get_boot_device to skip HV call 0x5B.

    Replaces 'sc 1' with hardcoded register writes and NOPs the
    subsequent comparison branches.

    Two code paths are patched:
      - Path 1 (sys/flash/boot): returns 8-byte device ID
      - Path 2 (ss/param/analog): returns 1-byte value

    device_id: value to write into r30 (default 0x190 = NAND)
    """
    lv2_base = 0x8000000000000000

    patch_sites = [
        {
            'name': 'sys/flash/boot',
            'li_r11': 0x226674,
            'sc':     0x226678,
            'cmpdi':  0x22667c,
            'bne':    0x226680,
            'mr':     0x226684,
        },
        {
            'name': 'ss/param/analog',
            'li_r11': 0x226768,
            'sc':     0x22676c,
            'cmpdi':  0x226770,
            'bne':    0x226774,
            'mr':     0x226778,
        },
    ]

    for site in patch_sites:
        name = site['name']
        for instr_name, offset in site.items():
            if instr_name == 'name':
                continue
            vaddr = lv2_base + offset
            data = write_word(data, vaddr, 0x60000000)  # nop
            if not data:
                print(f'[-] Failed to patch {instr_name} at 0x{vaddr:x} for {name}')
                return None

        vaddr = lv2_base + site['li_r11']
        data = write_word(data, vaddr, 0x38600000)  # li r3, 0
        if not data:
            return None

        vaddr = lv2_base + site['sc']
        data = write_word(data, vaddr, 0x3BC00000 | (device_id & 0xFFFF))  # li r30, device_id
        if not data:
            return None

        print(f'[+] Patched HV call at {name}: skipping sc, r3=0, r30=0x{device_id:x}')

    return data


def main():
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <lv2_decrypted.elf> [output.elf]')
        print(f'')
        print(f'Patches:')
        print(f'  1. Skip HV call 0x5B in sys_ss_get_boot_device,')
        print(f'     return hardcoded device ID (default 0x190 = NAND)')
        sys.exit(1)

    elf_path = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) > 2 else None

    if out_path is None:
        base = os.path.splitext(elf_path)[0]
        out_path = f'{base}_patched.elf'

    data = read_elf(elf_path)
    print(f'[*] Read {elf_path}: {len(data)} bytes')

    data = patch_hv_call(data)
    if data is None:
        print('[-] Patching failed')
        sys.exit(1)

    write_elf(out_path, data)
    print(f'[+] Patched ELF written to {out_path}')


if __name__ == '__main__':
    main()
