#!/usr/bin/env python

def partOne(input):
    total = 0

    visible = [[False for col in range(len(input[0]))] for row in range(len(input))]

    # check rows
    i = 0 
    while i < len(input):
        j = 0
        
        maxValue = 0
        while j < len(input[0]):
            if input[i][j] > maxValue:
                visible[i][j] = True
            
            maxValue = max(maxValue, input[i][j])
            j += 1
        
        maxValue = 0
        j = len(input[0]) - 1
        while j > 0: 
            if input[i][j] > maxValue:
                visible[i][j] = True
            
            maxValue = max(maxValue, input[i][j])
            j -= 1
        
        i += 1

    # Check columns 
    j = 0
    while j < len(input[0]):
        i = 0 
        maxValue = 0
        while i < len(input):
            if input[i][j] > maxValue:
                visible[i][j] = True
            
            maxValue = max(maxValue, input[i][j])
            i += 1
        
        maxValue = 0 
        i = len(input) - 1
        while i > 0:
            if input[i][j] > maxValue:
                visible[i][j] = True 

            maxValue = max(maxValue, input[i][j])
            i -= 1

        j += 1
    
    count = 0 
    for line in visible:
        count += len(filter(lambda x: x, line))
    return count

def calculateScore(row, col, input):
    leftCount = 0
    rightCount = 0
    topCount = 0
    bottomCount = 0

    # check left
    j = col - 1
    while j >= 0: 
        leftCount += 1
        if input[row][j] >= input[row][col]:
            break
        j -= 1
    print(leftCount)

    # check right
    j = col + 1
    while j < len(input[0]):
        rightCount += 1
        print('DEBUG')
        print(input[row][j])
        print(input[row][col])
        if input[row][j] >= input[row][col]:
            break
        j += 1
    print(rightCount)

    # check top
    i = row - 1
    while i >= 0:
        topCount += 1
        if input[i][col] >= input[row][col]:
            break
        i -= 1
    print(topCount)

    # check bottom
    i = row + 1
    while i < len(input):
        bottomCount += 1
        if input[i][col] >= input[row][col]:
            break
        i += 1
    print(bottomCount)

    return leftCount * rightCount * topCount * bottomCount

def partTwo(input):
    maxScore = 0

    i = 0
    while i < len(input):

        j = 0
        while j < len(input[0]):
            maxScore = max(maxScore, calculateScore(i, j, input))
            j += 1

        i += 1 

    return maxScore

def main(): 
    f = open('./input/day-8.txt', 'r')
    input = f.read().splitlines()

    inputMatrix = map(lambda x: list(x), input)
    
    print(partOne(inputMatrix))
    print(partTwo(inputMatrix))
        


if __name__ == '__main__':
    main()