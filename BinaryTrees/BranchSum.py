'''
Given a binary tree. 
Return sum of all of its branches.

'''

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    ans = []
    traverse(root, [], ans)
    return ans

def traverse(node, branch, ans) :
    if not node :
        return
    if not node.left and not node.right :
        ans.append(sum(branch) + node.value)
        return

    branch.append(node.value)
    traverse(node.left, branch, ans)
    traverse(node.right, branch, ans)
    branch.pop()

# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#-----------------------------------------------------
def branchSums(root):
    ans = []
    traverse(root, 0, ans)
    return ans

def traverse(node, branch, ans) :
    if not node :
        return
    if not node.left and not node.right :
        ans.append(branch + node.value)
        return

    
    traverse(node.left, branch + node.value, ans)
    traverse(node.right, branch + node.value, ans)
    #branch.pop()