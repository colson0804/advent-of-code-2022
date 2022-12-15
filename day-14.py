#!/usr/bin/env python

def drawPath(path, caveSet):
    previous = None
    for vertex in path:
        [x, y] = map(lambda x: int(x), vertex.split(','))
        if previous:
            [xprev, yprev] = previous
            print(previous, x, y)
            for i in range(min(xprev, x), max(xprev, x)+1):
                for j in range(min(yprev, y), max(yprev, y)+1):
                    caveSet.add((i, j))
            
        previous = [x, y]

    return caveSet

def partOne(input):
    caveSet = set()
    for line in input:
        path = line.split(' -> ')
        caveSet = drawPath(path, caveSet)

    grainsAtRest = 0
    start = (500, 0)

    while True:
        y = start[0]
        grain = start
        while y >= 0:
            # move down until, it's in the set 
            # then check bottom-left, then bottom-right
            y -= 1

    return 0

def partTwo(input):
    return 0

def main(): 
    f = open('./input/day-14.txt', 'r')
    input = f.read().splitlines()

    print(partOne(input))
    print(partTwo(input))

if __name__ == '__main__':
    main()