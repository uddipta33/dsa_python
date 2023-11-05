#You have been given a singly linked list of integers along with an integer 'N'. Write a function to append the last 'N' nodes towards the front of the singly linked list and returns the new head to the list.
from mymodule import *

def appendN(head,n):
    if(head is None):
        return head
    length = lengthLL(head)
    tail = None
    temp = head
    while(temp.next!=None):
        temp = temp.next
    tail = temp
    index = (length-n)-1
    count=0
    ptr = head
    while(count<index):
        ptr = ptr.next
        count+=1
    a = ptr.next
    ptr.next = None
    tail.next = head
    head = a
    return head


head = takeInput()
head = appendN(head,2)
printLL(head)