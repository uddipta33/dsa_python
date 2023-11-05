import re
from mymodule import *

def reverse(head):
    if(head is None or head.next == None):
        return head
    smallHead = reverse(head.next)
    tail = head.next 
    tail.next = head
    head.next = None
    return smallHead

head = takeInput()
head = reverse(head)
printLL(head)