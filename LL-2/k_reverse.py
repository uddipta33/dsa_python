from mymodule import *

def reverseK(head,k):
    if(head is None):
        return head
    prev = None
    curr = head
    front = None
    count = 0
    while(curr!=None and count<k):
        front = curr.next 
        curr.next = prev
        prev = curr
        curr = front
        count+=1
    if(front!=None):
        smallHead = reverseK(front, k)
        head.next = smallHead
    return prev

head = takeInput()
head = reverseK(head,3)
printLL(head)        