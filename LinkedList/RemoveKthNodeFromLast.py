"""
Given head of linked list and integer k,
remove kth node from last.
If node to be removed is head, swap head value with next node
"""

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    prev = None
    p = head
    q = head
    while k > 0 :
        p = p.next
        k -= 1
    while p :
        prev = q
        q = q.next
        p = p.next
    if prev :
        prev.next = q.next
    else :
        head.value = head.next.value
        head.next = head.next.next

