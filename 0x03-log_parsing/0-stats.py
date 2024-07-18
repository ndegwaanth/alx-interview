#!/usr/bin/python3
import sys
import signal

total_file_size = 0
status_codes_count = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}


def print_stats():
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes_count):
        if status_codes_count[code] > 0:
            print(f"{code}: {status_codes_count[code]}")


def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

line_count = 0

for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) < 10:
            continue

        ip_address = parts[0]
        date = parts[3][1:]
        request = parts[5] + " " + parts[6] + " " + parts[7]
        status_code = int(parts[8])
        file_size = int(parts[9])

        if request != '"GET /projects/260 HTTP/1.1"':
            continue

        total_file_size += file_size
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print_stats()

    except Exception as e:
        continue

print_stats()
