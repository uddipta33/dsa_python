#You have been given a singly linked list of integers. Write a function that returns the index/position of integer data denoted by 'N' (if it exists). Return -1 otherwise.

from mymodule import *

def find(head,n):
    if(head is None):
        return -1
    ptr = head
    index=0
    while(ptr!=None):
        if(ptr.data==n):
            return index
        ptr=ptr.next
        index+=1
    return -1

head = takeInput()
index = find(head,30)
print(index)


