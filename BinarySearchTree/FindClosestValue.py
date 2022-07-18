'''
Given a BST, and an integer, find node which has value closest to given integer.
You can assume tree will have only one closest value.
'''

#BFS

from collections import deque
import math
def findClosestValueInBst(tree, target):
    ans = 0
    prevDiff = math.inf
    data = deque()
    data.append(tree)
    while data :
        node = data.popleft()
        diff = abs(target - node.value)
        if diff < prevDiff :
            prevDiff = diff
            ans = node.value
        if node.left and target < node.value:
            data.append(node.left)
        elif node.right and target > node.value:
            data.append(node.right)
            
    return ans


# DFS
def findClosestValueInBst(tree, target):
   return traverse(tree, target, tree.value)

def traverse(node, target, prev) :
    if node is None :
        return prev    
    val = node.value
    if abs(target - val) < abs(target - prev) :
        prev = val
    if target < node.value :
        return traverse(node.left, target, prev)
    else :
        return traverse(node.right, target, prev)

# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


