'''
Given a binary tree, return its diameter.
Diameter of a binary tree is defined as lenght of its longest path even if that path doesn't pass through the root node.
'''

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    return binaryTreeDiameterHelper(tree)[1]

def binaryTreeDiameterHelper(tree):
    if not tree :
        return [0, 0] #hieght, maxDiaSoFar
    left = binaryTreeDiameterHelper(tree.left)
    right = binaryTreeDiameterHelper(tree.right)

    height = max(left[0], right[0]) + 1 #hieght of current node
    dia = max(left[0] + right[0], left[1], right[1]) #left[0] + right[0] = Dia of current node. keeping only max diameter yet.
    return [height, dia]

