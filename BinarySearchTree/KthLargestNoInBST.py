# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

'''
Using min heap
Not recommended
'''
import heapq
def findKthLargestValueInBst(tree, k):
    data = []
    traverse(tree, k, data)
    return data[0]
def traverse(node, k, data) :
    if node is None :
        return
    if len(data) < k :
        heapq.heappush(data, node.value)
    elif node.value >= data[0] :
        heapq.heappop(data)
        heapq.heappush(data, node.value)
    traverse(node.left, k, data)
    traverse(node.right, k, data)
        

'''
Recommanded approach.
Binary tree already have sorted values.
If you do inorder traversal, you will get array in sorted order.
This is faster (O(n)) time.
'''

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    data = inOrderTraverse(tree, [])
    return data[len(data) - k]

def inOrderTraverse(tree, data) :
    if tree :
        inOrderTraverse(tree.left, data)
        data.append(tree.value)
        inOrderTraverse(tree.right, data)
    return data