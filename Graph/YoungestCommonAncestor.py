'''
Given three nodes. 
One is top ancestor and other two are decendants.
Find and return common ancestor
'''

# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


# O(d) time - d is depth 
# O(n) space - no of ancestors
#using set to keep track of visited nodes, so can identify which node is common
def getYoungestCommonAncestor(top, nodeA, nodeB):
    vis = set()
    while nodeA : 
        vis.add(nodeA.name)
        nodeA = nodeA.ancestor
    while nodeB.name not in vis :
        vis.add(nodeB.name)
        nodeB = nodeB.ancestor
    return nodeB
   
        

# finding depth of both nodes
# traversing one node till both nodes are at same depth
# traversing both nodes together to find common ancestor

# O(d) time - d is depth
# O(1) space
def getYoungestCommonAncestor(top, nodeA, nodeB):
    d1 = getDepth(nodeA)
    d2 = getDepth(nodeB)
    diff = abs(d1 - d2)
    if d1 > d2 :
        while diff >= 0 :
            diff -= 1
            if nodeA.ancestor == nodeB :
                return nodeB
            nodeA = nodeA.ancestor
    elif d2 > d1 :
        while diff >= 0 :
            diff -= 1
            if nodeB.ancestor == nodeA :
                return nodeA
            nodeB = nodeB.ancestor
    while not (nodeA == top or nodeB == top) :
        if nodeA == nodeB.ancestor :
            return nodeA
        if nodeB == nodeA.ancestor :
            return nodeB
        if nodeA == nodeB :
            return nodeA
        nodeA = nodeA.ancestor
        nodeB = nodeB.ancestor
        
    return top

def getDepth(node) :
    depth = 0
    temp = node
    while temp :
        depth += 1
        temp = temp.ancestor
    return depth
