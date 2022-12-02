#!/usr/bin/env python

def partOne(input):
    maxValue = 0 
    i = 0 

    curr = 0
    while (i < len(input)):
        if not input[i]:
            maxValue = max(maxValue, curr)
            curr = 0
            i += 1
            continue

        curr += int(input[i])
        i += 1 

    return maxValue

def partTwo(input):
    maxValue = 0
    curr = 0
    maxArray = []
    for line in input:
        if not line:
            maxArray.append(curr)
            if len(maxArray) > 3:
                maxArray.sort()
                maxArray.pop(0)

            curr = 0
            continue

        curr += int(line)

    return sum(maxArray)

def main(): 
    f = open('./input/day-1.txt', 'r')
    input = f.read().splitlines()
    
    print(partOne(input))
    print(partTwo(input))
        


if __name__ == '__main__':
    main()