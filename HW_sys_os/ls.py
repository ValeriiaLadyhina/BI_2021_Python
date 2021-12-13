#!/usr/bin/env python
import argparse
import os


def file_search(args):
    files = os.listdir(dir_name)
    for file in files:
        if args.all:
            print(file)
        else:
            if file[0] == '.':
                pass
            else:
                print(file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--all', action='store_true',
                        help='count all files including hidden ones (starting with .)')
    parser.add_argument('dir_name',  help='name of directory you want to check', nargs='?', const='.')
    args = parser.parse_args()
    dir_name = args.dir_name
    file_search(args)

