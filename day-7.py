#!/usr/bin/env python

def partOne(root):
    visited = { root }

    total = 0
    stack = [root]

    while stack:
        curr = stack.pop()
        if isinstance(curr, DirectoryNode) and curr.children: 
            for child in curr.children:
                if child not in visited:
                    visited.add(child)
                    stack.insert(0, child)
            total += curr.totalSize()
        else:
            stack.pop() 

        print(stack)

    return total

def partTwo(input):
    return 0

class Node(object):
    def __init__(self, name, parent):
        self.name = name
        self.children = []
        self.parent = parent

    def getParent(self):
        return self.parent
    
    def printTree(self):
        print(self.name)

        if isinstance(self, DirectoryNode):
            for child in self.children:
                child.printTree()

    def totalSize(self, limit=100000):
        return 0
        
    
class DirectoryNode(Node):
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []

    def getChildNode(self, name):
        for child in self.children:
            if child.name == name:
                return child

        print('ERROR: Couldn\`t retrieve child node')
        return None

    def addDirectory(self, name):
        directory = DirectoryNode(name, self)
        self.children.append(directory)
    
    def addFile(self, name, size):
        file = FileNode(name, size, self)
        self.children.append(file)

    def totalSize(self, limit=100000):
        print(self.name + ' total size')
        sum = 0
        for child in self.children:
            sum += int(child.totalSize(limit))
        print(sum)
        if sum <= limit:
            return sum
        else:
            return 0

class FileNode(Node):
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent

    def totalSize(self, limit=100000):
        return int(self.size)


def buildTree(input):
    root = DirectoryNode('/', None)
    currentNode = root
    for line in input:
        components = line.split()
        if components[0] == '$':
            if components[1] == 'cd':
                if components[2] == '..':
                    currentNode = currentNode.getParent()
                elif components[2] == '/':
                    # Already handled this 
                    continue
                else:
                    currentNode = currentNode.getChildNode(components[2])
            elif components[1] == 'ls':
                continue
            else: 
                print('ERROR: Invalid command')
        else: 
            if components[0] == 'dir':
                currentNode.addDirectory(components[1])
            else:
                currentNode.addFile(components[1], components[0])
    return root

def main(): 
    f = open('./input/day-7.txt', 'r')
    input = f.read().splitlines()

    rootNode = buildTree(input)
    
    print(partOne(rootNode))
    print(partTwo(input))

if __name__ == '__main__':
    main()


