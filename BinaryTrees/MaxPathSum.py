'''
Given a binary tree, find its max path sum.


'''


'''
Branch sum - Any node has 2 paths. Left and right. We select one branch which has maximum sum inorder to get maximum path sum.

Path sum = For any subtree, there can be total 4 paths.
    Only node itself.
    Node + left path
    Node + right path
    Node + left path + right path.

We keep maximum sum of all paths at each sub tree,
'''
import math
def maxPathSum(tree):
    return maxPathSumHelper(tree)[1]

def maxPathSumHelper(tree):
    if not tree :
        return [0,-math.inf] #[sum of a branch with max sum, max path sum till now ]
    left = maxPathSumHelper(tree.left)
    right = maxPathSumHelper(tree.right)
    sum = max(left[0], right[0]) + tree.value #selecting a path with maximum sum at this node
    maxSumSoFar = max(maxVal(tree.value, left[0], right[0]), left[1], right[1]) # max sum of all subtrees beneath this and all possible 4 paths at this node
    return [sum, maxSumSoFar]

def maxVal(a,b,c) :
   return max(a, a+b, a+c, a+b+c)