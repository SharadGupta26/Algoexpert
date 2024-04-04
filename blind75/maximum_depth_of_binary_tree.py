'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.recur(root)

    def recur(self, node) :
        if not node :
            return 0
        a = self.recur(node.left)
        b = self.recur(node.right)
        return 1 + max(a,b)
