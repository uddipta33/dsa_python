#You have been given a singly linked list of integers where the elements are sorted in ascending order. Write a function that removes the consecutive duplicate values such that the given list only contains unique elements and returns the head to the updated list.
from os import remove
from mymodule import *

def removeDup(head):
    if(head is None):
        return head
    p1 = head
    p2 = head.next
    while(p2!=None):
        if(p1.data == p2.data):
            p1.next = p2.next
            a=p2
            p2 = p2.next
            a.next = None
        else:
            p1 = p2
            p2 = p2.next
    return head

head = takeInput()
head = removeDup(head)
printLL(head)