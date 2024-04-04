'''https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.traverse(root, p , q)

    def traverse(self, root, p,q) :
        if not root :
            return root
        
        if p.val < root.val and q.val < root.val :
            return self.traverse(root.left, p,q)
        elif p.val > root.val and q.val > root.val :
            return self.traverse(root.right, p,q)
        else :
            return root
        
        