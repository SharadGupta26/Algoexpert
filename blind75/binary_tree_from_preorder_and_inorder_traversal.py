'''https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/'''

#works when tree contains only unique values

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        indexes = {}
        for i in range(len(inorder)) :
            indexes[inorder[i]] = i
        return self.build(0, 0, len(inorder)-1, preorder, inorder, indexes)[0]

    def build(self, i, l, r, preorder, inorder, index) :
        if r < l:
            return (None,i-1)
        root = TreeNode(preorder[i])
        inorderIndex = index[preorder[i]]
        left, i = self.build(i+1, l, inorderIndex-1, preorder, inorder,index)
        right, i = self.build(i+1, inorderIndex+1, r, preorder, inorder, index)
        root.left = left
        root.right = right
        return (root,i)


#another solution where we split the inorder array
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        indexes = {}
        for i in range(len(inorder)) :
            indexes[inorder[i]] = i
        return self.build(preorder, inorder, indexes)

    def build(self, preorder, inorder, index) :
        if inorder :
            inorderIndex = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[inorderIndex])
            left = self.build( preorder, inorder[0:inorderIndex],index)
            right = self.build(preorder, inorder[inorderIndex+1:], index)
            root.left = left
            root.right = right
            return root