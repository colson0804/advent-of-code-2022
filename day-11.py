#!/usr/bin/env python

class Monkey:
    def __init__(self, items, operation, test):
        self.items = items
        self.operation = operation 
        self.test = test
        self.numberOfInspections = 0

    def takeTurn(self, anxietyReduce=True): # returns index of monkey to send item to 
        currentItem = int(self.items.pop(0))
        if currentItem:
            value = self.operation(currentItem)
            if anxietyReduce:
                value = int(value / 3)
            dest = self.test(value)
            self.numberOfInspections += 1
            return [value, dest]
        else:
            print("This monkey isn't holding any items")
            return [None, -1]
    
    def printMonkey(self):
        print(self.items)

    @staticmethod
    def buildMonkey(inputText):
        items = []
        operation = lambda x: x 
        test = lambda x: x
        dests = []
        modulo = 1

        for line in inputText.splitlines():
            print(line)
            match line.strip()[:5]:
                case "Start":
                    print("Here")
                    items = line[18:].split(", ")
                case "Opera": # operation
                    operation = eval(f"lambda old: {line[19:]}")
                case "Test:":
                    modulo = int(line.rsplit(" ", 1)[-1])
                case "If tr" | "If fa":
                    dests.append(int(line.rsplit(" ", 1)[-1]))
                    if len(dests) == 2:
                        test = eval(f'lambda x: {dests[0]} if x % {modulo} == 0 else {dests[1]}')
                        dests = []

        return Monkey(items, operation, test)

def partOne(input):
    monkeys = []
    for line in input:
        monkeys.append(Monkey.buildMonkey(line))
    
    for round in range(0, 20):
        for monkey in monkeys:
            while monkey.items:
                [item, dest] = monkey.takeTurn()
                monkeys[dest].items.append(item)
    
    for monkey in monkeys:
        monkey.printMonkey()
    
    monkeys = sorted(monkeys, key=lambda x: x.numberOfInspections, reverse=True)

    return monkeys[0].numberOfInspections * monkeys[1].numberOfInspections

def partTwo(input):
    monkeys = []
    for line in input:
        monkeys.append(Monkey.buildMonkey(line))
    
    for round in range(0, 10000):
        for monkey in monkeys:
            while monkey.items:
                [item, dest] = monkey.takeTurn(False)
                monkeys[dest].items.append(item)
    
    for monkey in monkeys:
        monkey.printMonkey()
    
    monkeys = sorted(monkeys, key=lambda x: x.numberOfInspections, reverse=True)

    return monkeys[0].numberOfInspections * monkeys[1].numberOfInspections

def main(): 
    f = open('./input/day-11.txt', 'r')
    input = f.read().split('\n\n')
    
    print(partOne(input))
    print(partTwo(input))
        


if __name__ == '__main__':
    main()