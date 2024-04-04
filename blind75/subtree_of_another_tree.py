'''https://leetcode.com/problems/subtree-of-another-tree/description/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot :
            return True
        return self.traverse(root, subRoot)

    def traverse(self, root, subroot) :
        if not root :
            return False
        ans = False
        if root.val == subroot.val :
            ans = self.check(root, subroot)
            
        if not ans :
            ans = self.traverse(root.left, subroot)

        if not ans :
            ans = self.traverse(root.right, subroot)
        return ans

    def check(self, root, subroot) :
        if not root and not subroot :
            return True
        if root and subroot and root.val == subroot.val :
            return self.check(root.left, subroot.left) and self.check(root.right, subroot.right)
        return False