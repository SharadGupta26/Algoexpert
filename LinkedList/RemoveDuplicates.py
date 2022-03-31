"""
Remove duplicates from given singly linked list
"""

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    temp = linkedList	
    while linkedList and linkedList.next :
        if linkedList.value == linkedList.next.value :
            linkedList.next = linkedList.next.next
        else :
            linkedList = linkedList.next
    return temp

