#!/usr/bin/env python3
import sys
import re


def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0
pattern = re.compile(
    r'^\d+\.\d+\.\d+\.\d+ - \[.+\] "GET /projects/260 HTTP/1\.1" \d+ \d+$'
)

try:
    for line in sys.stdin:
        line = line.strip()
        if pattern.match(line):
            parts = line.split()
            try:
                total_size += int(parts[-1])
                code = int(parts[-2])
                if code in status_codes:
                    status_codes[code] += 1
            except (ValueError, IndexError):
                pass
            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)
except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    raise
