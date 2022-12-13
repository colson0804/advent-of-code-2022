#!/usr/bin/env python

def findStart(input):
    i = 0 
    while i < len(input):
        j = 0
        while j < len(input[0]):
            if input[i][j] == "S":
                return (i, j)
            j += 1
        
        i += 1
    
    return (-1, -1)

def partOne(input):
    queue = []
    visited = [[False for _ in range(len(input[0]))] for _ in range(len(input))]
    dist = [[100000 for _ in range(len(input[0]))] for _ in range(len(input))]
    pred = [['-1' for _ in range(len(input[0]))] for _ in range(len(input))]

    src = findStart(input)

    visited[src[0]][src[1]] = True
    dist[src[0]][src[1]] = 0
    queue.append(src)

    while len(queue) > 0:
        curr = queue.pop(0)
        adj = [(curr[0] - 1, curr[1]), (curr[0] + 1, curr[1]), (curr[0], curr[1] - 1), (curr[0], curr[1] + 1)]
        for adjacent in adj:
            if adjacent[0] < 0 or adjacent[0] >= len(input) or adjacent[1] < 0 or adjacent[1] >= len(input[0]):
                continue

            if ((ord(input[adjacent[0]][adjacent[1]]) <= (ord(input[curr[0]][curr[1]]) + 1) or curr == src)
                and (input[adjacent[0]][adjacent[1]] != 'E' or input[curr[0]][curr[1]] == 'z')):
                if not visited[adjacent[0]][adjacent[1]]:
                    visited[adjacent[0]][adjacent[1]] = True
                    dist[adjacent[0]][adjacent[1]] = dist[curr[0]][curr[1]] + 1
                    pred[adjacent[0]][adjacent[1]] = curr

                    queue.append(adjacent)

                    if input[adjacent[0]][adjacent[1]] == 'E':
                        return dist[adjacent[0]][adjacent[1]]

    return -1

def partTwo(input):
    return 0

def formatInput(input):
    output = []
    for line in input:
        output.append(list(line))
    return output

def main(): 
    f = open('./input/day-12.txt', 'r')
    input = formatInput(f.read().splitlines())
    
    print(partOne(input))
    print(partTwo(input))
        


if __name__ == '__main__':
    main()