"""
Given two linked list representing nos, add them and return new linked list represent sum
"""

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    head = LinkedList(-1)
    node = head
    cf = 0
    while linkedListOne and linkedListTwo :
        value = cf + linkedListOne.value + linkedListTwo.value
        node.next = LinkedList(value % 10)
        node = node.next
        cf = value // 10
        linkedListOne = linkedListOne.next
        linkedListTwo = linkedListTwo.next
        
    while linkedListOne :
        value = cf + linkedListOne.value 
        node.next = LinkedList(value % 10)
        node = node.next
        cf = value // 10
        linkedListOne = linkedListOne.next
        
    while linkedListTwo :
        value = cf + linkedListTwo.value 
        node.next = LinkedList(value % 10)
        node = node.next
        cf = value // 10
        linkedListTwo = linkedListTwo.next
        
    if cf > 0 :
        node.next = LinkedList(cf)

    return head.next


def sumOfLinkedLists_2(linkedListOne, linkedListTwo):
    head = LinkedList(-1)
    node = head
    cf = 0
    while linkedListOne or linkedListTwo or cf != 0 :
        a = linkedListOne.value if linkedListOne is not None else 0
        b = linkedListTwo.value if linkedListTwo is not None else 0
        value = cf + a + b
        node.next = LinkedList(value % 10)
        node = node.next
        cf = value // 10
        linkedListOne = linkedListOne.next if linkedListOne is not None else None
        linkedListTwo = linkedListTwo.next if linkedListTwo is not None else None
        
    return head.next
