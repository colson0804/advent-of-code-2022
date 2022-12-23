#!/usr/bin/env python

import os
import time
import sys
import operator

NUMBER_OF_ROCKS = 5

ROCK_LOCATIONS = set()
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
        if not isFalling:
            ROCK_LOCATIONS.add(point)

def shiftRock(rock, operator):
    newRock = set()

    for point in rock:
        if operator == '<':
            if min(map(lambda x: x[1], rock)) > 0:
                newY = point[1] - 1
                newPoint = (point[0], newY)
                if newPoint not in ROCK_LOCATIONS:
                    newRock.add(newPoint)
                else:
                    return rock
            else:
                return rock
        elif operator == '>':
            if max(map(lambda x: x[1], rock)) + 1 < len(CAVE[0]):
                newY = point[1] + 1
                newPoint = (point[0], newY)
                if newPoint not in ROCK_LOCATIONS:
                    newRock.add(newPoint)
                else:
                    return rock
            else:
                return rock
    return newRock

def dropRock(rock):
    # we're checking the lower bounds outside of this method
    newRock = set()
    for point in rock:
        newPoint = (point[0] + 1, point[1])
        if newPoint not in ROCK_LOCATIONS:
            newRock.add(newPoint)
        else:
            return (rock, False)
    return (newRock, True)

def highPoint():
    if ROCK_LOCATIONS:
        return max(map(lambda x: x[0], ROCK_LOCATIONS))
    else:
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
    jetPos = 0

    printCave()

    for i in range(0, NUMBER_OF_ROCKS):
        time.sleep(1)

        currentRock = spawnRock(i)

        placeRock(currentRock, True)
        printCave()

        while True:
            time.sleep(0.5)

            clearRock(currentRock)

            currentRock = shiftRock(currentRock, input[jetPos])
            jetPos = (jetPos + 1) % len(input)

            if max(map(lambda x: x[0], currentRock)) < highPoint():
                (currentRock, didDrop) = dropRock(currentRock)
                if not didDrop: # blech
                    placeRock(currentRock, False)
                    break
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