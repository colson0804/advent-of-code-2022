#!/usr/bin/env python

import os
import time
import sys

NUMBER_OF_ROCKS = 5

CAVE = [['.' for _ in range(0, 7)] for _ in range(0, 10)]

def printCave():
    for row in CAVE:
        print("|" + ''.join(row) + "|")
    
    print("+-------+")

def clearCave():
    global CAVE
    CAVE = [['.' for _ in range(0, 7)] for _ in range(0, 10)]

def printRock(rock, isFalling):
    for point in rock:
        CAVE[point[0]][point[1]] = "@" if isFalling else "#"
    
    printCave()

def spawnRock(rock):
    highPoint = len(CAVE) - 1
    i = 0
    while i < len(CAVE):
        for space in CAVE[i]:
            if space == "#":
                highPoint = i 
        i += 1

    rockBottom = max(map(lambda x: x[0], rock))

    newRock = set()
    for point in rock:
        displacement = highPoint - 3 - rockBottom
        newRock.add((point[0] + displacement, point[1]))
    
    return newRock


def partOne(input):
    rocks = [set([(0, 2), (0, 3), (0, 4), (0, 5)]), set([(0, 3), (1, 2), (1, 3), (1, 4), (2, 3)]), set([(0, 4), (1, 4), (2, 2), (2, 3), (2, 4)]), set([(0, 2), (1, 2), (2, 2), (3, 2)]), set([(0, 2), (0, 3), (1, 2), (1, 3)])]
    # Create block at (0, 2)

    j = 0 

    printCave()

    for i in range(0, NUMBER_OF_ROCKS):
        jetPos = j % len(input)
        currentRock = rocks[i % len(rocks)]

        currentRock = spawnRock(currentRock)

        printRock(currentRock, True)

        clearCave()

    #     while True: # while not on floor 
    #         if input[jetPos] == "<":
    #             # move left 
    #             print("left")
    #         elif input[jetPos] == ">":
    #             print("right")

    #         j += 1 

    #         # if can move down 
    #         # move down 
    #         # else go to next rock 


    
    return 0

def partTwo(input):
    return 0

def main(): 
    f = open('./input/day-17.txt', 'r')
    input = f.read()

    print(partOne(input))
    print(partTwo(input))

if __name__ == '__main__':
    main()