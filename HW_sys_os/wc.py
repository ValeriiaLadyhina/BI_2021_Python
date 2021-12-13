#!/usr/bin/env python3
import argparse
import re
import sys


def counter(args, file):
    lines = 0
    words = 0
    characters = 0
    for line in file:
        if args.lines:
            lines += 1
            words = None
            characters = None
        elif args.words:
            words += word_counter(line)
            lines = None
            characters = None
        elif args.characters:
            characters += len(line)
            words = None
            lines = None
        else:
            lines += 1
            words += word_counter(line)
            characters += len(line)
    return lines, words, characters


def word_counter(line):
    pattern = re.compile(r'\b\w+\b')
    return len(re.findall(pattern, line))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--lines', action='store_true', help='line count')
    parser.add_argument('-w', '--words', action='store_true', help='word count')
    parser.add_argument('-c', '--characters', action='store_true', help='character count')
    parser.add_argument('file', metavar='FILE', nargs='*', help='input file', default='-')
    args = parser.parse_args()
    if args.file == '-':
        file = sys.stdin
    else:
        file = open(args.file).readlines()
    lines, words, characters = counter(args, file)
    if args.lines:
        print(lines, args.file)
    elif args.words:
        print(words, args.file)
    elif args.characters:
        print(characters, args.file)
    else:
        print(lines, words, characters, args.file)
