from collections import deque

#BFS solution
def invertBinaryTree(tree):
    if not tree :
        return tree
    data = deque()
    data.append(tree)
    while data :
        node = data.popleft()
        node.left, node.right = node.right, node.left
        if node.left :
            data.append(node.left)
        if node.right :
            data.append(node.right)
    return tree
            

#DFS solution
def invertBinaryTree(tree):
    if not tree : 
        return None
    tree.left, tree.right = tree.right, tree.left
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)
    return tree


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

