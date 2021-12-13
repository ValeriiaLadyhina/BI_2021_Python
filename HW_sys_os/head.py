#!/usr/bin/env python3
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', nargs='?',
                        help='to show other number of lines', default='-')
    parser.add_argument('number',   action='store_true',
                        help='number of lines to be shown', default='-')
    parser.add_argument('file',  help='file/files to process to show', nargs='+', default='-')
    args = parser.parse_args()
    n = args.n
    if n == '-':
        file = args.file
        file = open(file).readlines()
        print(file)
        if len(file) < 10:
            for line in range(len(file)):
                print(file[line])
        else:
            for line in range(10):
                print(file[line])
    else:
        number = args.number
        print(number)
        for i in range(0, len(args.file)):
            file = args.file[i]
            file = open(file).readlines()
            if len(file) < int(number):
                for line in range(len(file)):
                    print(file[line])
            else:
                for line in range(int(number)):
                    print(file[line])