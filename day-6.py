#!/usr/bin/env python

def containsDuplicates(subarray):
    return len(set(subarray)) < len(subarray)

def partOne(input):
    i = 0
    while i < len(input):
        if i < 4:
            i += 1
            continue 
        
        if not containsDuplicates(input[i - 4:i]):
            return i

        i += 1

    return 0

def partTwo(input):
    i = 0
    while i < len(input):
        if i < 14:
            i += 1
            continue 
        
        if not containsDuplicates(input[i - 14:i]):
            return i

        i += 1

    return 0

def main(): 
    f = open('./input/day-6.txt', 'r')
    input = f.read()
    
    print(partOne(input))
    print(partTwo(input))
        


if __name__ == '__main__':
    main()