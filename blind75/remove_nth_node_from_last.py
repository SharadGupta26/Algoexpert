'''https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(-1, head)
        left = temp
        right = head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right :
            left = left.next
            right = right.next
        left.next = left.next.next
        return temp.next 