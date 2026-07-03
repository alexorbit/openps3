#!/usr/bin/env python3
"""
Disassemble a PPC64 (or PPC32) ELF using Capstone.

Usage: python3 ps3_disasm.py <elf_file> [output.txt] [--count N]

Scans all executable LOAD segments and writes Capstone disassembly
to a text file. Use --count to limit total instructions.
"""

import sys
import os
sys.path.insert(0, '/home/alexorbit/.local/lib/python3.12/site-packages')

from capstone import Cs, CS_ARCH_PPC, CS_MODE_32, CS_MODE_64, CS_MODE_BIG_ENDIAN
import struct


def disasm_elf(elf_path, output_path=None, count=0):
    with open(elf_path, 'rb') as f:
        data = f.read()

    if data[:4] != b'\x7fELF':
        print('Not a valid ELF file')
        return False

    e_type = struct.unpack('>H', data[0x10:0x12])[0]
    e_machine = struct.unpack('>H', data[0x12:0x14])[0]
    e_entry = struct.unpack('>Q', data[0x18:0x20])[0]
    e_phoff = struct.unpack('>Q', data[0x20:0x28])[0]
    e_phentsize = struct.unpack('>H', data[0x36:0x38])[0]
    e_phnum = struct.unpack('>H', data[0x38:0x3A])[0]

    if e_machine == 21:
        arch = CS_ARCH_PPC
        mode = CS_MODE_64 | CS_MODE_BIG_ENDIAN
        arch_name = 'PowerPC64 (BE)'
    elif e_machine == 20:
        arch = CS_ARCH_PPC
        mode = CS_MODE_32 | CS_MODE_BIG_ENDIAN
        arch_name = 'PowerPC32 (BE)'
    else:
        print(f'Unsupported machine: 0x{e_machine:x}')
        return False

    total_exec = 0
    segments = []
    for i in range(e_phnum):
        off = e_phoff + i * e_phentsize
        p_type = struct.unpack('>I', data[off:off+4])[0]
        p_flags = struct.unpack('>I', data[off+4:off+8])[0]
        p_offset = struct.unpack('>Q', data[off+8:off+16])[0]
        p_vaddr = struct.unpack('>Q', data[off+16:off+24])[0]
        p_filesz = struct.unpack('>Q', data[off+32:off+40])[0]

        if p_type == 1:
            s = {'offset': p_offset, 'vaddr': p_vaddr, 'size': p_filesz, 'flags': p_flags}
            segments.append(s)
            if p_flags & 1:
                total_exec += p_filesz

    print(f'Arch: {arch_name}')
    print(f'Type: {"EXEC" if e_type == 2 else "DYN" if e_type == 3 else e_type}')
    print(f'Entry: 0x{e_entry:016x}')
    print(f'Executable: {total_exec} bytes ({total_exec/1024/1024:.1f} MB)')

    if output_path is None:
        base = os.path.splitext(os.path.basename(elf_path))[0]
        output_path = f'{base}_disasm.txt'

    print(f'Disassembling -> {output_path}')

    md = Cs(arch, mode)
    md.detail = False
    md.skipdata = True

    total_insns = 0
    with open(output_path, 'w') as out:
        out.write(f'; Disassembly of {os.path.basename(elf_path)}\n')
        out.write(f'; Arch: {arch_name}  Entry: 0x{e_entry:016x}\n\n')

        for seg in segments:
            if not (seg['flags'] & 1):
                continue

            code = data[seg['offset']:seg['offset']+seg['size']]
            out.write(f'\n{"="*80}\n')
            out.write(f'; LOAD seg: vaddr=0x{seg["vaddr"]:016x}  offset=0x{seg["offset"]:x}  size=0x{seg["size"]:x}\n')
            out.write(f'{"="*80}\n\n')

            insn_count = 0
            for insn in md.disasm(code, seg['vaddr']):
                out.write(f'  0x{insn.address:016x}:  {insn.mnemonic:10s} {insn.op_str}\n')
                total_insns += 1
                insn_count += 1
                if count > 0 and total_insns >= count:
                    break

            if count > 0 and total_insns >= count:
                out.write(f'\n; (stopped after {count} instructions total)\n')
                break
            elif count == 0:
                out.write(f'\n; ({insn_count} instructions in segment)\n')

    print(f'Done: {total_insns} instructions -> {output_path}')
    return True


def main():
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <elf_file> [output.txt] [--count N]')
        sys.exit(1)

    elf_path = sys.argv[1]
    output_path = None
    count = 0
    i = 2
    while i < len(sys.argv):
        a = sys.argv[i]
        if a == '--count' and i+1 < len(sys.argv):
            count = int(sys.argv[i+1])
            i += 2
        elif not a.startswith('--'):
            output_path = a
            i += 1
        else:
            i += 1

    disasm_elf(elf_path, output_path, count=count)


if __name__ == '__main__':
    main()
