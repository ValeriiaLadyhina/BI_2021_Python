#!/usr/bin/env python3
import os
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p',  '--parents',  action='store_true',
                        help='no error if existing, make parent directories as needed')
    parser.add_argument('dir_name', help='name of directory you want to check', nargs='?', const='.')
    args = parser.parse_args()
    dir_name = args.dir_name
    p = args.parents
    if p:
        os.makedirs(dir_name, exist_ok=True)
    else:
        os.mkdir(dir_name)
