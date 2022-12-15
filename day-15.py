#!/usr/bin/env python

import re

def matchLine(line):
    # return (sensor location, beacon location)
    row = re.sub("[^0-9=-]","", line)[1:].split('=')
    sx, sy, bx, by = row 
    return ((int(sx), int(sy)), (int(bx), int(by)))

def partOne(input):
    y = 2000000 
    positions = set()

    for line in input:
        (sensor, beacon) = matchLine(line)
        bDist = abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])
        yDist = abs(y - sensor[1])
        if yDist <= bDist:
            for i in range(sensor[0] - (bDist - yDist), sensor[0] + (bDist - yDist)):
                positions.add(i)

    return len(positions)

def partTwo(input):
    return 0

def main(): 
    f = open('./input/day-15.txt', 'r')
    input = f.read().splitlines()

    print(partOne(input))
    print(partTwo(input))

if __name__ == '__main__':
    main()