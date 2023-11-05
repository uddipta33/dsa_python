#You have been given a singly linked list of integers. Write a function to print the list in a reverse order.
#To explain it further, you need to start printing the data from the tail and move towards the head of the list, printing the head data at the end.
from mymodule import *

def printReverse(head):
    if(head is None):
        return
    printReverse(head.next)
    print(head.data)

head = takeInput()
printReverse(head)