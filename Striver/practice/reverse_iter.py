from LL_initial import *

def reverse(head):
    if head is None or head.next == None:
        return head
    prev = None
    curr = head
    fut = head.next 
    while(curr!=None):
        curr.next = prev
        prev = curr
        curr = fut
        if(fut!=None):
            fut = fut.next 
    return prev

head = takeInput()
head = reverse(head)
printLL(head)