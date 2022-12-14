#!/usr/bin/env python

import json
from functools import cmp_to_key

def compare(left, right): 
    # return 1 if inputs are in correct order, -1 if not, 0 if they are equal 
        
    match (isinstance(left, list), isinstance(right, list)):
        case True, True:
             match (left, right):
                case ([x, *_], [y, *_]):
                    match compare(x, y):
                        case -1:
                            return -1
                        case 0:
                            return compare(left[1:], right[1:])
                        case 1:
                            return 1
                case ([x, *_], []):
                    return -1
                case ([], [y, *_]):
                    return 1
                case ([], []):
                    return 0
        case True, False:
            return compare(left, [right])
        case False, True:
            return compare([left], right)
        case False, False:
            if left < right:
                return 1
            elif right < left:
                return -1
            else:
                return 0


def partOne(input):
    input = input.split('\n\n')

    result = 0
    i = 0
    while i < len(input):
        (left, right) = map(lambda x: json.loads(x), input[i].splitlines())
        result += (i + 1) if compare(left, right) == 1 else 0
        i += 1
    return result

def partTwo(input):
    a = [[2]]
    b = [[6]]

    input = list(map(lambda x: json.loads(x), list(filter(None, input.splitlines()))))
    input.append(a)
    input.append(b)

    compare_key = cmp_to_key(compare)
    sortedInput = sorted(input, key=compare_key, reverse=True)

    print(sortedInput)

    return (sortedInput.index(a) + 1) * (sortedInput.index(b) + 1)

def main(): 
    f = open('./input/day-13.txt', 'r')
    input = f.read()

    print(partOne(input))
    print(partTwo(input))

if __name__ == '__main__':
    main()