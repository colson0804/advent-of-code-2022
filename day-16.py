#!/usr/bin/env python

import re

def partOne(input):
    for line in input:
        print(line)

    return 0

def partTwo(input):
    return 0

def main(): 
    f = open('./input/day-16.txt', 'r')
    input = f.read().splitlines()

    print(partOne(input))
    print(partTwo(input))

if __name__ == '__main__':
    main()