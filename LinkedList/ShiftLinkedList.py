"""
Given a linked list and value k, shift its nodes forward or backward in place.
Shift list forward if k > 0 else shift list backward
"""

# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

"""
Algo :
find linked list length
convert linked list to cyclic linked list by connecting tail.next = head
Given K is no of rotation. Find no of nodes that will be shifted right (r) after k rotation.
find rth node. rth node next will be new head.

"""
def shiftLinkedList(head, k):
    n = 1
    last = head
    while last.next :
        n += 1
        last = last.next
    last.next = head

    r = k % n
    if r >= 0 :
        r = n-r-1
        
    #print(k,n,r)
    temp = head
    while r > 0:
        r -= 1
        temp = temp.next
    head = temp.next
    temp.next = None
    return head