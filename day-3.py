#!/usr/bin/env python

def findCommonCharacter(s1, s2):
    if len(s1) != len(s2):
        print("Invalid input")
        return -1

    hash = {} # {character: bool}

    i = 0 
    while i < len(s1):
        hash[s1[i]] = True
        i += 1
    
    j = 0 
    while j < len(s2):
        if hash.has_key(s2[j]):
            return getCharacterValue(s2[j])
        j += 1

    print("No common characters")
    return -1

def getCharacterValue(char, problem = 1):
    asciiValue = ord(char)
    if asciiValue >= 65 and asciiValue <= 90:
        return asciiValue - (65 - 27)
    elif asciiValue >= 97 and asciiValue <= 122:
        return asciiValue - 96

def partOne(input):
    result = 0
    for line in input:
        comp1, comp2 = line[:len(line)//2], line[len(line)//2:]
        
        result += findCommonCharacter(comp1, comp2)   

    return result

def findCommonCharacter2(s1, s2, s3):
    dict = {} # character: count 

    i = 0 
    while i < len(s1):
        dict[s1[i]] = 1
        i += 1

    j = 0 
    while j < len(s2):
        if s2[j] in dict and dict[s2[j]] == 1:
            dict[s2[j]] = 2
        
        j += 1

    k = 0
    while k < len(s3):
        if s3[k] in dict and dict[s3[k]] == 2:
            dict[s3[k]] = 3
            return getCharacterValue(s3[k], 2)
        
        k += 1

    print("Invalid input")
    return -1

def partTwo(input):
    result = 0 

    i = 0 
    while i < len(input):
        result += findCommonCharacter2(input[i], input[i + 1], input[i + 2])
        i += 3

    return result 

def main():
    f = open('./input/day-3.txt', 'r')
    input = f.read().splitlines()

    print("Result part 1: " + str(partOne(input)))
    print("Result part 2: " + str(partTwo(input)))

if __name__ == '__main__':
    main()