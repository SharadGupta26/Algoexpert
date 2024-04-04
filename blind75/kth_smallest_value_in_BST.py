'''https://leetcode.com/problems/kth-smallest-element-in-a-bst/'''

#using max heap
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from heapq import heappush,heappop
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        self.recur(root, heap, k)
        return -1 * heap[0]

    def recur(self,  root, heap, k) :
        if not root :
            return 
        val = root.val * (-1)
        
        if len(heap) == k :
            if val > heap[0] :
                heappop(heap)
                heappush(heap, val)
        else :
            heappush(heap, val)
        self.recur(root.left, heap, k)
        self.recur(root.right, heap, k)



# using BST property and iterative DFS

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while root or stack :
            while root :
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0 :
                return root.val
            root = root.right
        return -1
            
