#!/usr/bin/env python

def partOne(input):
    result = 0 

    for line in input:
        [opponent, player] = line.split()
        result += matchOutcome(opponent, player) + selectedShape(player)

    return result

def selectedShape(player):
    if player == 'X':
        return 1
    elif player == 'Y':
        return 2
    elif player == 'Z':
        return 3

    print("Failed to recognize player input")
    return 0

def matchOutcome(opponent, player):
    if (opponent == 'A' and player == 'Y') or (opponent == 'B' and player == 'Z') or (opponent == 'C' and player == 'X'):
        print(opponent + ' ' + player + ' WIN')
        return 6 
    elif (opponent == 'A' and player == 'X') or (opponent == 'B' and player == 'Y') or (opponent == 'C' and player == 'Z'):
        print(opponent + ' ' + player + ' TIE')
        return 3
    else: 
        print(opponent + ' ' + player + ' LOSS')
        return 0

def partTwo(input):
    result = 0 

    for line in input:
        [opponent, outcome] = line.split()
        result += matchOutcome2(outcome) + selectedShape2(opponent, outcome)

    return result

def matchOutcome2(outcome):
    if outcome == 'X':
        return 0
    elif outcome == 'Y':
        return 3
    elif outcome == 'Z':
        return 6
    
    print("Invalid input")
    return 0

def selectedShape2(opponent, desiredOutcome):
    if desiredOutcome == 'X': 
        if opponent == 'A':
            return 3
        elif opponent == 'B':
            return 1
        else:
            return 2
    elif desiredOutcome == 'Y':
        if opponent == 'A':
            return 1
        elif opponent == 'B':
            return 2 
        elif opponent == 'C':
            return 3 
    else: 
        if opponent == 'A':
            return 2
        elif opponent == 'B':
            return 3 
        else:
            return 1
    return 0

def main():
    f = open('./input/day-2.txt', 'r')
    input = f.read().splitlines()

    print("Result part 1: " + str(partOne(input)))
    print("Result part 2: " + str(partTwo(input)))

if __name__ == '__main__':
    main()