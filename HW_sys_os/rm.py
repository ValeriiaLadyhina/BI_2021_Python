#!/usr/bin/env python3
import argparse
import os
import shutil


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', action='store_true',
                        help='recursively remove non-empty directory')
    parser.add_argument('path', help='path to file/directory to be removed', nargs='?', const='.')
    args = parser.parse_args()
    if args.r:
        shutil.rmtree(args.path)
    elif os.path.isfile(args.path):
        os.remove(args.path)
    elif os.path.isdir(args.path):
        os.removedirs(args.path)
