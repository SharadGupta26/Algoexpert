

#my solution
#creating a temp head node

# This is an input class. Do not edit.
from sys import ps2


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    p = headOne
    q = headTwo
    head = LinkedList(0)
    temp = head
    while p and q :
        if p.value <= q.value :
            temp.next = p
            p = p.next
        else :
            temp.next = q
            q = q.next
        temp = temp.next
    while p :
        temp.next = p
        p = p.next
        temp = temp.next
    while q :
        temp.next = q
        q = q.next
        temp = temp.next
    return head.next

#algo expert solution
def mergeLinkedLists_2(headOne, headTwo):
    p = headOne
    q = headTwo
    prev = None

    while p and q :
        if p.value < q.value :
            prev = p
            p = p.next
        else :
            if prev :
                prev.next = q
            prev = q
            prev.next = p
            q = q.next
    return headOne if headOne.value < headTwo.value else headTwo
