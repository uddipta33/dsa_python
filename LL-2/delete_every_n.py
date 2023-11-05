#You have been given a singly linked list of integers along with two integers, 'M,' and 'N.' Traverse the linked list such that you retain the 'M' nodes, then delete the next 'N' nodes. Continue the same until the end of the linked list.

from mymodule import *

def delete(head,m,n):
    if(head is None):
        return head
    mptr = None
    nptr = None
    ptr = head
    
    