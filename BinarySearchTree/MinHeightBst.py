'''
Given a sorted array. Create a min height BST and return root node of tree
'''

def minHeightBst(array):
    return createBst(array, 0, len(array) - 1)

def createBst(array, i, j) :
    if i <= j :
        mid = (i + j) // 2 
        root = BST(array[mid])
        root.left = createBst(array, i, mid - 1)
        root.right = createBst(array, mid+1, j)
        return root
    else :
        return None

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
def minHeightBst(array):
    return createBst(array, 0, len(array) - 1)

def createBst(array, i, j) :
    if i <= j :
        mid = (i + j) // 2 
        root = BST(array[mid])
        root.left = createBst(array, i, mid - 1)
        root.right = createBst(array, mid+1, j)
        return root
    else :
        return None

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
