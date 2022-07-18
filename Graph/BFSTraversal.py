'''
Given head of acyclic graph, preform BFS traversal.
'''

# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
from collections import deque
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        data = deque()
        data.append(self)
        while data :
            node = data.popleft()
            array.append(node.name)
            for i in node.children :
                data.append(i)
        return array
