#!/usr/bin/env python

import os
import time
import sys
import operator

NUMBER_OF_ROCKS = 5

CAVE = [['.' for _ in range(0, 7)] for _ in range(0, 10)]
ROCK_STARTING_POSITIONS = [set([(0, 2), (0, 3), (0, 4), (0, 5)]), set([(0, 3), (1, 2), (1, 3), (1, 4), (2, 3)]), set([(0, 4), (1, 4), (2, 2), (2, 3), (2, 4)]), set([(0, 2), (1, 2), (2, 2), (3, 2)]), set([(0, 2), (0, 3), (1, 2), (1, 3)])]

def printCave():
    os.system("clear")
    for row in CAVE:
        sys.stdout.write("|" + ''.join(row) + "|\n")
    
    sys.stdout.write("+-------+\n")
    sys.stdout.flush()

def clearCave():
    global CAVE
    CAVE = [['.' for _ in range(0, 7)] for _ in range(0, 10)]

def clearRock(rock):
    global CAVE
    for point in rock:
        CAVE[point[0]][point[1]] = '.'

def placeRock(rock, isFalling):
    for point in rock:
        CAVE[point[0]][point[1]] = "@" if isFalling else "#"

def shiftRock(rock, operator):
    newRock = set()
    for point in rock:
        if operator == '<':
            if min(map(lambda x: x[1], rock)) > 0:
                newY = point[1] - 1
                newRock.add((point[0], newY))
            else:
                return rock
        elif operator == '>':
            if max(map(lambda x: x[1], rock)) + 1 < len(CAVE[0]):
                newY = point[1] + 1
                newRock.add((point[0], newY))
            else:
                return rock
    return newRock

def dropRock(rock):
    # we're checking the lower bounds outside of this method
    newRock = set()
    for point in rock:
        newRock.add((point[0] + 1, point[1]))
    return newRock

def highPoint():
    i = 0
    while i < len(CAVE):
        for space in CAVE[i]:
            if space == "#":
                return i
        i += 1
    
    return len(CAVE) - 1

def spawnRock(iteration):
    rock = ROCK_STARTING_POSITIONS[iteration % len(ROCK_STARTING_POSITIONS)]

    rockBottom = max(map(lambda x: x[0], rock))

    newRock = set()
    for point in rock:
        displacement = highPoint() - 3 - rockBottom
        newRock.add((point[0] + displacement, point[1]))
    
    return newRock


def partOne(input):
    j = 0 

    printCave()

    for i in range(0, NUMBER_OF_ROCKS):
        time.sleep(1)

        jetPos = j % len(input)
        currentRock = spawnRock(i)

        placeRock(currentRock, True)
        printCave()

        # clearCave()

        while True:
            time.sleep(0.5)

            # clearCave()
            clearRock(currentRock)

            currentRock = shiftRock(currentRock, input[jetPos])
            j += 1
            jetPos = j % len(input)

            # if currentRock[]
            if max(map(lambda x: x[0], currentRock)) < highPoint():
                currentRock = dropRock(currentRock)
                # restRock
            else: 
                placeRock(currentRock, False)
                break

            placeRock(currentRock, True)
            printCave()

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