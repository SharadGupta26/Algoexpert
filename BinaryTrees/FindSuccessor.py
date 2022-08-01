'''
Given a binary tree and a node return the given node's successor.
Each node has pointer to its parent node too.
A node's successor is the next node to be visited (immedietely after the given node) when traversing the tree using 
in-order traversal.

'''


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

'''
Solution - 
If given node has any right subtree, then next node to be visited in inorder traversal is left most node of its right subtree.
If node don't has any right subtree, then we need to check, in which node's left sub tree this node lies.
If there is no such node (node does not exist in any node's left sub tree) then node in question is last node to be visited.
'''
def findSuccessor(tree, node):
    if node.right :
        return leftmost(node.right)
    parent = node.parent
    while parent :
        exist = existInLeftTree(parent.left, node)
        if exist :
            return parent
        parent = parent.parent
    return None

def leftmost(tree) :
    if not tree.left :
       return tree 
    return leftmost(tree.left)

def existInLeftTree(tree, node) :
    if not tree :
        return False
    if tree == node :
        return True
    return existInLeftTree(tree.left, node) or existInLeftTree(tree.right, node)