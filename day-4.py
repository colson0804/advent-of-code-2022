#!/usr/bin/env python

def parseLine(line):
    # returns tuple of tuples ie [[3, 4], [6, 8]]
    return tuple(map(lambda x: map(lambda y: int(y), x.split('-')), tuple(line.split(','))))

def partOne(input):
    result = 0
    for line in input:
        ranges = parseLine(line)
        if (ranges[0][0] <= ranges[1][0] and ranges[0][1] >= ranges[1][1]) or (ranges[0][0] >= ranges[1][0] and ranges[0][1] <= ranges[1][1]):
            result += 1

    return result

def partTwo(input):
    result = 0
    for line in input:
        ranges = parseLine(line)
        # do the ranges not NOT overlap?
        if not ((ranges[0][1] < ranges[1][0]) or (ranges[0][0] > ranges[1][1])):
            print(ranges)
            result += 1

    return result

def main():
    f = open('./input/day-4.txt', 'r')
    input = f.read().splitlines()

    print("Result part 1: " + str(partOne(input)))
    print("Result part 2: " + str(partTwo(input)))

if __name__ == '__main__':
    main()