'''https://leetcode.com/problems/binary-tree-level-order-traversal/description/'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        data = deque()
        data.append(root)
        ans = []
        while data :
            size = len(data)
            level = []
            while size :
                size -= 1
                node = data.popleft()
                if node :
                    level.append(node.val)
                    data.append(node.left)
                    data.append(node.right)
            if level :
                ans.append(level)
        return ans
        