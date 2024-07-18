#!/usr/bin/python3
import sys

total_size = 0
status_codes = {}

for i, line in enumerate(sys.stdin):
    try:
        _, _, _, _, _, status_code, file_size = line.split()
        status_code = int(status_code)
        file_size = int(file_size)
        total_size += file_size
        status_codes[status_code] = status_codes.get(status_code, 0) + 1
    except ValueError:
        continue

    if (i + 1) % 10 == 0:
        print(f"File size: {total_size}")
        for code in sorted(status_codes.keys()):
            print(f"{code}: {status_codes[code]}")

try:
    for line in sys.stdin:
        pass
except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")
