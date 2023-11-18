#!/usr/bin/env python
import sys

def read_csv(filepath):
    with open(filepath, "r") as f:
        content = f.read()
        rows = content.split('\n')[1:]
        data = [row.split(',') for row in rows]
        return (rows)

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python main.py <argument>")
        sys.exit(1)

    # Access the argument
    file = sys.argv[1]
    print(read_csv(file))

if __name__ == "__main__":
    main()