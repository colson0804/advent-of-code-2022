#!/usr/bin/env python

def updateTail(tail, head):
    # if tail and head are adjacent
    if tail[0] >= head[0] - 1 and tail[0] <= head[0] + 1 and tail[1] >= head[1] - 1 and tail[1] <= head[1] + 1:
        return tail
    elif tail[0] == head[0]:
        if tail[1] < head[1]: 
            return (tail[0], tail[1] + 1)
        else:
            return (tail[0], tail[1] - 1)
    elif tail[1] == head[1]:
        if tail[0] < head[0]:
            return (tail[0] + 1, tail[1])
        else:
            return (tail[0] - 1, tail[1])

    else: 
        if head[0] > tail[0]:
            if head[1] > tail[1]:
                return (tail[0] + 1, tail[1] + 1)
            else:
                return (tail[0] + 1, tail[1] - 1)
        else:
            if head[1] > tail[1]:
                return (tail[0] - 1, tail[1] + 1)
            else:
                return (tail[0] - 1, tail[1] - 1)

    return tail

def partOne(input):
    visited = set((0, 0))
    head = (0,0)
    tail = (0,0)
    for line in input:
        [direction, steps] = line.split()
        print(line)
        for i in range(int(steps)):
            if direction == "R":
                head = (head[0], head[1] + 1)
            elif direction == "L":
                head = (head[0], head[1] - 1)
            elif direction == "U":
                head = (head[0] + 1, head[1])
            elif direction == "D":
                head = (head[0] - 1, head[1])
            else:
                print("Invalid direction")
            
            tail = updateTail(tail, head)
            visited.add(tail)
        
    return len(visited)

def partTwo(input):
    visited = set((0, 0))
    head = (0,0)
    body = [(0,0) for x in range(0, 9)]
    print(body)
    for line in input:
        [direction, steps] = line.split()
        print(line)
        for i in range(int(steps)):
            if direction == "R":
                head = (head[0], head[1] + 1)
            elif direction == "L":
                head = (head[0], head[1] - 1)
            elif direction == "U":
                head = (head[0] + 1, head[1])
            elif direction == "D":
                head = (head[0] - 1, head[1])
            else:
                print("Invalid direction")
            
            j = 0 
            while j < len(body):
                if j == 0:
                    body[j] = updateTail(body[j], head)
                else:
                    body[j] = updateTail(body[j], body[j - 1])
                
                j += 1
            
            visited.add(body[8])
        
    return len(visited)

def main(): 
    f = open('./input/day-9.txt', 'r')
    input = f.read().splitlines()
    
    print(partOne(input))
    print(partTwo(input))
        


if __name__ == '__main__':
    main()