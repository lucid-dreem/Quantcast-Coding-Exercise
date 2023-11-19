#!/usr/bin/env python
import argparse

def read_csv(filepath):
    with open(filepath, "r") as f:
        content = f.read()
        rows = content.split('\n')[1:]
        data = [row.split(',') for row in rows]
        return (data)

def processing(formatted_info, date):
    freq = {}
    for log in formatted_info:
        if date in log[1]:
            if log[0] in freq:
                freq[log[0]] += 1
            else:
                freq[log[0]] = 1
        elif freq:
            break

    max_val = 0
    if freq:
        max_val = max(freq.values())

    print_all_max(freq, max_val)

def print_all_max(freq_dict, max_val):
    for (key, val) in freq_dict.items():
        if val == max_val:
            print (key)


def main():
    parser = argparse.ArgumentParser()

    # Set up parameter recognition
    parser.add_argument('filename', help='cookie log CSV to format')
    parser.add_argument('-d', '--date', help='Input a date with format YYYY-MM-DD')

    # Parse to obtain arguments
    args = parser.parse_args()

    filename = args.filename
    date = args.date

    if not date:
        print("Date argument is required")
        parser.print_help()
        exit()

    data = read_csv(filename)
    processing(data, date)

if __name__ == "__main__":
    main()