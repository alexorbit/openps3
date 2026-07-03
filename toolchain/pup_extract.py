#!/usr/bin/env python3
"""
Extract segments from a PS3Update PUP file.

Usage: python3 pup_extract.py PS3UPDAT_4.93.PUP [output_dir]

Parses the PUP header and segment directory, extracts each segment
to individual files, and optionally extracts update_files.tar.
"""

import struct
import os
import sys


def parse_pup_header(data):
    magic = data[0:7]
    format_flag = data[7]
    package_version = struct.unpack('>Q', data[0x08:0x10])[0]
    image_version = struct.unpack('>Q', data[0x10:0x18])[0]
    segment_num = struct.unpack('>Q', data[0x18:0x20])[0]
    file_offset = struct.unpack('>Q', data[0x20:0x28])[0]
    file_size = struct.unpack('>Q', data[0x28:0x30])[0]
    return {
        'magic': magic,
        'format_flag': format_flag,
        'package_version': package_version,
        'image_version': image_version,
        'segment_num': segment_num,
        'file_offset': file_offset,
        'file_size': file_size,
    }


def parse_segment_entries(data, segment_num, base=0x30):
    entries = []
    known = {
        0x100: 'version.txt',
        0x101: 'license.xml',
        0x103: 'update_flags.txt',
        0x200: 'ps3swu.self',
        0x201: 'vsh.tar',
        0x202: 'dots.txt',
        0x300: 'update_files.tar',
        0x501: 'spkg_hdr.tar',
        0x601: 'ps3swu2.self',
    }
    for i in range(segment_num):
        off = base + i * 0x20
        entry_id = struct.unpack('>Q', data[off:off+8])[0]
        offset = struct.unpack('>Q', data[off+0x08:off+0x10])[0]
        size = struct.unpack('>Q', data[off+0x10:off+0x18])[0]
        sign_alg = struct.unpack('>I', data[off+0x18:off+0x1C])[0]
        entries.append({
            'id': entry_id,
            'name': known.get(entry_id, f'unknown_0x{entry_id:x}'),
            'offset': offset,
            'size': size,
            'sign_algorithm': sign_alg,
        })
    return entries


def main():
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <PS3UPDAT.PUP> [output_dir]')
        sys.exit(1)

    pup_path = sys.argv[1]
    out_dir = sys.argv[2] if len(sys.argv) > 2 else 'pup_extracted'

    with open(pup_path, 'rb') as f:
        data = f.read()

    hdr = parse_pup_header(data)
    entries = parse_segment_entries(data, hdr['segment_num'])

    print(f'Magic: {hdr["magic"].decode("ascii", errors="replace")}')
    print(f'Format Flag: {hdr["format_flag"]}')
    print(f'Package Version: {hdr["package_version"]}')
    print(f'Image Version: {hdr["image_version"]}')
    print(f'Segment Count: {hdr["segment_num"]}')
    print(f'Header Size: {hdr["file_offset"]}')
    print(f'Data Size: {hdr["file_size"]}')
    print(f'File Size: {hdr["file_offset"] + hdr["file_size"]}')

    os.makedirs(out_dir, exist_ok=True)

    for entry in entries:
        start = entry['offset']
        end = start + entry['size']
        ext = '.bin'
        if entry['name'].endswith('.self'):
            ext = '.self'
        elif entry['name'].endswith('.tar'):
            ext = '.tar'
        elif entry['name'].endswith('.txt'):
            ext = '.txt'
        elif entry['name'].endswith('.xml'):
            ext = '.xml'
        fname = f'{entry["id"]:04x}_{entry["name"]}'
        fpath = os.path.join(out_dir, fname)
        print(f'[0x{entry["id"]:x}] {entry["name"]} @ 0x{entry["offset"]:x} size=0x{entry["size"]:x} ({entry["size"]} bytes) -> {fpath}')
        with open(fpath, 'wb') as f:
            f.write(data[start:end])

    print(f'\nExtracted {len(entries)} segments to {out_dir}/')

    tar_entry = [e for e in entries if e['name'] == 'update_files.tar']
    if tar_entry:
        tar_path = os.path.join(out_dir, f'{tar_entry[0]["id"]:04x}_update_files.tar')
        tar_out = os.path.join(out_dir, 'update_files')
        os.makedirs(tar_out, exist_ok=True)
        print(f'\nExtracting update_files.tar -> {tar_out}/')
        ret = os.system(f'tar -xf "{tar_path}" -C "{tar_out}" 2>&1')
        if ret != 0:
            print(f'tar extraction returned {ret}')
        else:
            for root, dirs, files in os.walk(tar_out):
                for fname in files:
                    fpath = os.path.join(root, fname)
                    print(f'  {fpath}')


if __name__ == '__main__':
    main()
