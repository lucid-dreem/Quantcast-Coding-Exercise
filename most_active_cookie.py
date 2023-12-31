#!/usr/bin/env python
import argparse

def read_csv(filepath):
    with open(filepath, "r") as f:
        content = f.read()
        rows = content.split('\n')[1:]
        data = [row.split(',') for row in rows]
        return (data)

def date_prev(date):
    day = date[-2:]
    month = date[5:7]
    year = date[:4]

    new_day = day
    new_month = month
    new_year = year

    if day == "01":
        if month in ["10", "05", "07", "12"]:
            new_day = "30"
            new_month = str(int(month) - 1)
        elif month == "03":
            new_month = "02"
            if int(year) % 4 == 0:
                new_day = "29"
            else:
                new_day = "28"
        elif month == "01":
            new_day = "31"
            new_month = "12"
            new_year = str(int(year) - 1)
        else:
            new_day = "31"
            new_month = str(int(month) - 1)
    else:
        new_day = str(int(day) - 1)

    if len(new_month) == 1:
        new_month = "0" + new_month
    
    if len(new_day) == 1:
        new_day = "0" + new_day
    
    return (new_year+"-"+new_month+"-"+new_day)

def on_date(date_field, date_target):
    if date_field[:10] == date_target:
        prev_flag = False
    elif date_field[:10] == date_prev(date_target):
        prev_flag = True
    else:
        return False

    hour, mins = int(date_field[-14:-12]), int(date_field[-11:-9])
    hour_add, min_add = int(date_field[-5:-3]), int(date_field[-2:])

    utc_next_day = (hour + hour_add >= 24) or (hour + hour_add == 23 and mins+min_add >= 60)

    # if it is the previous day and UTC conversion gives the target day
    # or if it is the target day and UTC conversion gives the target
    if prev_flag == utc_next_day:
        return True
    else:
        return False

def processing(formatted_info, date):
    freq = {}
    for log in formatted_info:
        if on_date(log[1], date):
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