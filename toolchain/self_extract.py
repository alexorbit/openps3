#!/usr/bin/env python3
"""
Extract embedded ELF from a decrypted PS3 SELF file.

Usage: python3 self_extract.py <decrypted.self> [output.elf]

The SELF must already be decrypted (e.g., using unself from fail0verflow PS3 tools).
This script locates the embedded ELF header and extracts the ELF data.
"""

import struct
import sys
import os


def extract_elf_from_self(self_path, out_path=None):
    with open(self_path, 'rb') as f:
        data = f.read()

    if data[0:4] != b'SCE\x00':
        print('Not a valid SELF file (magic != SCE\\0)')
        return False

    elf_start = None
    for i in range(0, min(0x200, len(data))):
        if data[i:i+4] == b'\x7fELF':
            elf_start = i
            break

    if elf_start is None:
        print('No ELF header found in SELF file')
        return False

    if data[elf_start+4] != 2:
        print(f'Not a 64-bit ELF (class={data[elf_start+4]})')
        return False

    e_shoff = struct.unpack('>Q', data[elf_start+0x28:elf_start+0x30])[0]
    e_shentsize = struct.unpack('>H', data[elf_start+0x3A:elf_start+0x3C])[0]
    e_shnum = struct.unpack('>H', data[elf_start+0x3C:elf_start+0x3E])[0]
    e_shstrndx = struct.unpack('>H', data[elf_start+0x3E:elf_start+0x40])[0]

    elf_size = e_shoff + (e_shnum * e_shentsize)
    elf_data = data[elf_start:elf_start+elf_size]

    if out_path is None:
        base = os.path.basename(self_path)
        name, _ = os.path.splitext(base)
        out_path = f'{name}.elf'

    with open(out_path, 'wb') as f:
        f.write(elf_data)

    e_entry = struct.unpack('>Q', data[elf_start+0x18:elf_start+0x20])[0]
    e_machine = struct.unpack('>H', data[elf_start+0x12:elf_start+0x14])[0]
    machine_map = {21: 'PPC64', 20: 'PPC', 43: 'SPU', 50: 'IA-64'}
    machine_name = machine_map.get(e_machine, f'Unknown(0x{e_machine:x})')

    print(f'ELF extracted: {out_path}')
    print(f'  Machine: {machine_name}')
    print(f'  Entry: 0x{e_entry:x}')
    print(f'  Sections: {e_shnum}')
    print(f'  ELF size: {elf_size} bytes (0x{elf_size:x})')
    print(f'  ELF offset in SELF: 0x{elf_start:x}')

    return True


def main():
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <self_file> [output.elf]')
        sys.exit(1)

    self_path = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) > 2 else None
    extract_elf_from_self(self_path, out_path)


if __name__ == '__main__':
    main()
