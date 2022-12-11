#!/usr/bin/env python

TEST_VALUES = { 20, 60, 100, 140, 180, 220 }

def partOne(input):
    counter = 0
    x = 1
    result = 0

    def incrementResult(result, counter, x):
        if counter in TEST_VALUES:
            result += counter * x

        return result

    for line in input:
        instruction = line.split()[0]

        if instruction == "addx":
            value = int(line.split()[1])

            for _ in range(0, 2):
                counter += 1
                result = incrementResult(result, counter, x)
            
            x += value

        elif instruction == "noop":
            counter += 1
            result = incrementResult(result, counter, x)
        
    return result

def updateOutput(output, counter, x, line):
        i = counter / 40
        j = counter % 40

        if i > 5: # blech 
            return output
        if j >= (x - 1) and j <= (x + 1):
            output[i][j] = "#"
        else:
            output[i][j] = "."

        return output

def formatOutput(output):
    outputText = ""
    for row in output:
        for col in row:
            outputText += col
        
        outputText += "\n"
    
    return outputText

def partTwo(input):
    counter = 0
    x = 1
    output = [['.' for _ in range(0, 40)] for _ in range(0, 6)]

    for line in input:
        instruction = line.split()[0]

        if instruction == "addx":
            value = int(line.split()[1])
            for _ in range(0, 1):
                counter += 1 
                output = updateOutput(output, counter, x, line)

            x += value
            counter += 1
            output = updateOutput(output, counter, x, line)

        elif instruction == "noop":
            counter += 1
            output = updateOutput(output, counter, x, line)
        
    return formatOutput(output)

def main(): 
    f = open('./input/day-10.txt', 'r')
    input = f.read().splitlines()
    
    print(partOne(input))
    print(partTwo(input))
        


if __name__ == '__main__':
    main()