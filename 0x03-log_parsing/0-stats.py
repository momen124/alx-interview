#!/usr/bin/python3
import sys

# Store the count of all status codes in a dictionary
status_codes_dict = {
    '200': 0, '301': 0, '400': 0, '401': 0,
    '403': 0, '404': 0, '405': 0, '500': 0
}

total_size = 0
count = 0  # Keep count of the number of lines processed

def print_stats():
    """ Print current statistics """
    print('File size: {}'.format(total_size))
    for code in sorted(status_codes_dict):
        if status_codes_dict[code] > 0:
            print('{}: {}'.format(code, status_codes_dict[code]))

try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) >= 7:
            try:
                status_code = line_list[-2]
                file_size = int(line_list[-1])

                if status_code in status_codes_dict:
                    status_codes_dict[status_code] += 1

                total_size += file_size

                count += 1
                if count == 10:
                    count = 0
                    print_stats()

            except (ValueError, IndexError):
                # Handle lines where file size is not an integer or missing
                continue

except KeyboardInterrupt:
    # Handle keyboard interruption
    print_stats()

finally:
    # Print final statistics when exiting
    print_stats()
