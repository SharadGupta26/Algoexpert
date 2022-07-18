'''
given a Head node of acyclic graph. return DFS traversal
'''

# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
       return self.DFS(self, array)
        
    def DFS(self, node, array) :
        array.append(node.name)
        for i in node.children :
            self.DFS(i, array)
        return array
