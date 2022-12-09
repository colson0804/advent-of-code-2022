#!/usr/bin/env python

# def partOne(root):
#     visited = { root }

#     total = 0
#     stack = [root]

#     while stack:
#         curr = stack.pop()
#         if isinstance(curr, DirectoryNode) and curr.children: 
#             for child in curr.children:
#                 if child not in visited:
#                     visited.add(child)
#                     stack.insert(0, child)
#             total += curr.totalSize()
#         else:
#             stack.pop() 

#         print(stack)

#     return total

# def partTwo(input):
#     return 0

# class Node(object):
#     def __init__(self, name, parent):
#         self.name = name
#         self.children = []
#         self.parent = parent

#     def getParent(self):
#         return self.parent
    
#     def printTree(self):
#         print(self.name)

#         if isinstance(self, DirectoryNode):
#             for child in self.children:
#                 child.printTree()

#     def totalSize(self, limit=100000):
#         return 0
        
    
# class DirectoryNode(Node):
#     def __init__(self, name, parent):
#         self.name = name
#         self.parent = parent
#         self.children = []

#     def getChildNode(self, name):
#         for child in self.children:
#             if child.name == name:
#                 return child

#         print('ERROR: Couldn\`t retrieve child node')
#         return None

#     def addDirectory(self, name):
#         directory = DirectoryNode(name, self)
#         self.children.append(directory)
    
#     def addFile(self, name, size):
#         file = FileNode(name, size, self)
#         self.children.append(file)

#     def totalSize(self, limit=100000):
#         print(self.name + ' total size')
#         sum = 0
#         for child in self.children:
#             sum += int(child.totalSize(limit))
#         print(sum)
#         if sum <= limit:
#             return sum
#         else:
#             return 0

# class FileNode(Node):
#     def __init__(self, name, size, parent):
#         self.name = name
#         self.size = size
#         self.parent = parent

#     def totalSize(self, limit=100000):
#         return int(self.size)


# def buildTree(input):
#     root = DirectoryNode('/', None)
#     currentNode = root
#     for line in input:
#         components = line.split()
#         if components[0] == '$':
#             if components[1] == 'cd':
#                 if components[2] == '..':
#                     currentNode = currentNode.getParent()
#                 elif components[2] == '/':
#                     # Already handled this 
#                     continue
#                 else:
#                     currentNode = currentNode.getChildNode(components[2])
#             elif components[1] == 'ls':
#                 continue
#             else: 
#                 print('ERROR: Invalid command')
#         else: 
#             if components[0] == 'dir':
#                 currentNode.addDirectory(components[1])
#             else:
#                 currentNode.addFile(components[1], components[0])
#     return root

# def main(): 
#     f = open('./input/day-7.txt', 'r')
#     input = f.read().splitlines()

#     rootNode = buildTree(input)
    
#     print(partOne(rootNode))
#     print(partTwo(input))

# if __name__ == '__main__':
#     main()


# from collections import defaultdict
# from queue import PriorityQueue
# from typing import DefaultDict, List, Set


# def create_file_tree(terminal_list: List[str]) -> DefaultDict:
#     tree: DefaultDict = defaultdict(lambda: {"parent": None, "size": 0, "type": "dir", "depth": 0})
#     cwd = "/"
#     for line in terminal_list:
#         line_split = line.split()
#         if line == "$ cd ..":
#             cwd = tree[cwd].get("parent", "/")
#         elif line == "$ cd /":
#             cwd = "/"
#         elif line.startswith("$ cd"):
#             cwd = f"{cwd}{line_split[-1]}/"
#         elif line_split[0] == "dir":
#             tree[f"{cwd}{line_split[-1]}/"]["parent"] = cwd
#             tree[f"{cwd}{line_split[-1]}/"]["depth"] = tree[cwd]["depth"] + 1
#         elif line_split[0].isdigit():
#             tree[f"{cwd}{line_split[-1]}"]["parent"] = cwd
#             tree[f"{cwd}{line_split[-1]}"]["depth"] = tree[cwd]["depth"] + 1
#             tree[f"{cwd}{line_split[-1]}"]["type"] = "file"
#             tree[f"{cwd}{line_split[-1]}"]["size"] = int(line_split[0])
#     return tree


# def bfs_fill_file_sizes(terminal_list: List[str]) -> DefaultDict:
#     file_tree = create_file_tree(terminal_list)
#     pqueue: PriorityQueue = PriorityQueue()
#     seen_objs: Set = set()
#     max_depth = max(obj["depth"] for obj in file_tree.values())
#     for leaf in [(fp, obj["depth"]) for fp, obj in file_tree.items() if obj["type"] == "file"]:
#         pqueue.put((max_depth - leaf[1], leaf[0]))
#     while not pqueue.empty():
#         cur_priority, cur_obj = pqueue.get()
#         if file_tree[cur_obj]["parent"] is not None and cur_obj not in seen_objs:
#             pqueue.put((cur_priority + 1, file_tree[cur_obj]["parent"]))
#             file_tree[file_tree[cur_obj]["parent"]]["size"] += file_tree[cur_obj]["size"]
#         seen_objs.add(cur_obj)
#     assert set(file_tree.keys()).difference(seen_objs) == set()
#     assert sum(obj["size"] for obj in file_tree.values() if obj["type"] == "file") == file_tree["/"]["size"]
#     return file_tree


# def part1(terminal_list: List[str]) -> int:
#     file_tree = bfs_fill_file_sizes(terminal_list)
#     return sum(obj["size"] for obj in file_tree.values() if obj["size"] <= 100000 and obj["type"] == "dir")




# def part2(terminal_list: List[str]) -> int:
#     file_tree = bfs_fill_file_sizes(terminal_list)
#     space_target = 30000000 + file_tree["/"]["size"] - 70000000
#     return min(obj["size"] for obj in file_tree.values() if obj["type"] == "dir" and obj["size"] >= space_target)



# print("Part 1: ", part1(open("./input/day-7.txt").read().split("\n")))
# print("Part 2: ", part2(open("./input/day-7.txt").read().split("\n")))