from mymodule import *

def reverse(head):
    if(head is None or head.next == None):
        return head
    prev = None
    curr = head
    front = head.next
    while(curr!=None):
        curr.next = prev
        prev = curr
        curr = front
        if(front!=None):
            front = front.next 
    return prev

head = takeInput()
head = reverse(head)
printLL(head)