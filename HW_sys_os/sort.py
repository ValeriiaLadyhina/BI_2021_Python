#!/usr/bin/env python3
import argparse
import sys


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', metavar='FILE', nargs='*', help='file to be sorted', default='-')
    args = parser.parse_args()
    file = args.file
    if file == '-':
        file = sys.stdin
        print(file)
    else:
        file = open(args.file).readlines()
    print(*sorted(file))
