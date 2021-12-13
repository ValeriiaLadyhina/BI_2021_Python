#!/usr/bin/env python3
import argparse
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()
    file = open(args.file).read()
    print(file)
    sys.stdout(file)
