from mymodule import *

def insert(head,i,data):
    if(head is None):
        return head
    if (i==0):
        n1 = Node(data)
        n1.next = head
        head = n1
        return head
    temp = head.next
    smallHead = insert(temp, i-1, data)
    head.next = smallHead
    return head

def delete(head,i):
    if(head is None):
        return head
    if(i==0):
        head = head.next
        return head
    smallHead = delete(head.next, i-1)
    head.next = smallHead
    return head

head = takeInput()
#head = insert(head, 2, 99)
head = delete(head, 2)
printLL(head)