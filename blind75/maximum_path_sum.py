'''https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
For explanation, watch https://www.youtube.com/watch?v=Hr5cWUld4vU
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, -math.inf)[1]
    
    def dfs(self, root, maxVal) :
        if not root :
            return (0,maxVal)
        left, leftMaxVal = self.dfs(root.left, maxVal)
        right, rightMaxVal= self.dfs(root.right, maxVal)
        left = max(left, 0)
        right = max(right,0)

        maxVal = max(maxVal,leftMaxVal, rightMaxVal, root.val + left + right)
        retVal = max(left, right) + root.val
        return (retVal, maxVal)



#more clean solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [root.val]

        def dfs(root) :
            if not root :
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            left = max(left, 0)
            right = max(right,0)

            #max sum of path current sub tree(left + root + right)
            ans[0] = max(ans[0], root.val + left + right)

            #when returning, we can choose only one path either left or right
            retVal = max(left, right) + root.val
            return retVal
        dfs(root)
        return ans[0]
    
    