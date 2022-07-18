
'''
Given a Tree, validate if its a BST.
For a BST, every node in left is strictly smaller than the node and every node in right is strictly greather or equeal to node.
'''

# This is an input class. Do not edit.
import math
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return validateBstHelper(tree.left, -math.inf, tree.value) and validateBstHelper(tree.right, tree.value, math.inf)

def validateBstHelper(node, minValue, maxValue) :
    if node is None :
        return True
    if node.value < minValue  or node.value >= maxValue :
        return False
    print(node.value, minValue, maxValue)
    left = node.left
    right = node.right
    return validateBstHelper(left, minValue, node.value) and validateBstHelper(right, node.value, maxValue)