#!/usr/bin/env python3
import argparse
import sys
import re
import os


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('pattern', help='pattern that you want to search')
    parser.add_argument('path', metavar='FILE', nargs='?', help='file or dictionary in which you need to search',
                        default='-')
    args = parser.parse_args()
    path = args.path
    pattern = args.pattern
    pattern = re.compile(pattern)
    if os.path.isfile(path):
        file = open(path).read()
        print(type(pattern))
        for line in file:
            result = pattern.match(line)
            print(result)


