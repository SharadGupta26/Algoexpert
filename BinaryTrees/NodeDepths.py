'''
Given a binary tree, find sum of depth of each node.
'''

def nodeDepths(root):
   return nodeDepthsHelper(root, 0)

def nodeDepthsHelper(root, depth):
    if not root :
        return 0
    if not root.left and not root.right :
        return depth
    return depth + nodeDepthsHelper(root.left, 1+depth) + nodeDepthsHelper(root.right, 1 + depth)
    

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

