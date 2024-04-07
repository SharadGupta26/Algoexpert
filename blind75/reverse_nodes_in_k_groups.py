'''https://leetcode.com/problems/reverse-nodes-in-k-group/description/'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []
        ans = ListNode()
        temp = ans
        
        prev = head
        while head :
            if len(stack) < k :
                prev = head
                i = k
                while i > 0 and head:
                    i -= 1
                    stack.append(head)
                    head = head.next
                
            if len(stack) == k :
                while stack :
                    temp.next = stack.pop()
                    temp = temp.next
                    temp.next = None

        if stack and len(stack) < k :
            temp.next = prev
        
        return ans.next
