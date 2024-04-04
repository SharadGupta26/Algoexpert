'''https://leetcode.com/problems/validate-binary-search-tree/description/
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root :
            return True
        return self.isValid(root.left, -math.inf, root.val) and self.isValid(root.right, root.val, math.inf)

    def isValid(self, root, low, high) :
        if not root :
            return True
        if root.val <= low or root.val >= high :
            return False
        return self.isValid(root.left, low, root.val) and  self.isValid(root.right, root.val, high)