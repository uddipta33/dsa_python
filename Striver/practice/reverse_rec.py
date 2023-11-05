from LL_initial import *

def reverseLL(head):
    if (head is None or head.next == None):
        return head
    smallHead = reverseLL(head.next)
    tail = head.next 
    tail.next = head
    head.next = None
    return smallHead

head = takeInput()
head = reverseLL(head)
printLL(head)