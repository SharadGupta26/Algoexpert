'''
Given a binary tree, check if it height balanced or not.
A binary tree is height balanced if for each node in tree, diff bw its height of left subtree
and right subtree is at most 1.

'''

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
   return getHeight(tree)[1]

def getHeight(tree) :
    if not tree :
        return (0,True)
    left = getHeight(tree.left)
    right = getHeight(tree.right)
    
    if not left[1] or not right[1]:
        return (0, False)
        
    if abs(left[0] - right[0]) > 1 :
        return (0, False)
        
    return (max(left[0], right[0]) + 1, True)
