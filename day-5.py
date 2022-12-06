#!/usr/bin/env python
import numpy as np
import re

def buildStacks(text):
    stackList = text.split('\n')
    stackList.pop() # Remove column numbers 

    matrix = map(lambda x: list(x), stackList)

    matrix = np.transpose(matrix)
    matrix = filter(lambda x: filter(lambda y: y.isalpha(), x), np.array(matrix).tolist())

    k = []
    for row in matrix:
        k.append(filter(lambda x: x.isalpha(), row))

    return k

def partOne(stacks, instructions):
    for instruction in instructions: 
        m = re.match(r'move (.*) from (.*) to (.*)', instruction)
        [numberToMove, sourceStack, destinationStack] = [int(m.group(1)), int(m.group(2)) - 1, int(m.group(3)) - 1]
        for _ in range(numberToMove):
            crate = stacks[sourceStack].pop(0)
            stacks[destinationStack].insert(0, crate)


    return "".join(map(lambda x: x[0], stacks))

def partTwo(stacks, instructions):
    for instruction in instructions:
        m = re.match(r'move (.*) from (.*) to (.*)', instruction)
        [numberToMove, sourceStack, destinationStack] = [int(m.group(1)), int(m.group(2)) - 1, int(m.group(3)) - 1]

        crates = stacks[sourceStack][:numberToMove]
        stacks[sourceStack] = stacks[sourceStack][numberToMove:]
        stacks[destinationStack][0:0] = crates


    return "".join(map(lambda x: x[0], stacks))

def main():
    f = open('./input/day-5.txt', 'r')
    [stackStr, instructions] = f.read().split('\n\n')

    stacks = buildStacks(stackStr)
    
    print(partOne(stacks, instructions.split('\n')))

    stacks = buildStacks(stackStr)
    print(partTwo(stacks, instructions.split('\n')))

if __name__ == '__main__':
    main()