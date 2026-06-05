#!/usr/bin/python3
""" Module log parsing """
import sys


def print_stats(total_size, status_code):
    """ Affiche les métriques accumulées """
    print("File size: {}".format(total_size))
    for key in sorted(status_code.keys()):
        if status_code[key] > 0:
            print("{}: {}".format(key, status_code[key]))


if __name__ == "__main__":
    total_size = 0
    status_code = {
        "200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
        "404": 0, "405": 0, "500": 0
    }
    counter = 0

    try:
        for line in sys.stdin:
            counter += 1
            try:
                parts = line.split()
                if len(parts) >= 2:
                    total_size += int(parts[-1])
                    code = parts[-2]
                    if code in status_code:
                        status_code[code] += 1
            except (IndexError, ValueError):
                pass

            if counter % 10 == 0:
                print_stats(total_size, status_code)

        print_stats(total_size, status_code)

    except KeyboardInterrupt:
        print_stats(total_size, status_code)
        raise
