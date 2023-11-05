from mymodule import *

def swap(head,i,j):
    if(head is None or head.next==None or i==j):
        return head
    pn1=None
    n1=head
    pn2=None
    n2=head
    count=0
    while(count<i):
        pn1=n1
        n1=n1.next 
        count+=1
    count=0
    while(count<j):
        pn2=n2
        n2=n2.next 
        count+=1
    a=n1.next 
    b=n2.next
    #for first element pn1 will be null so pn1.next will be wrong
    if(i==0):
        head=n2
        n2.next = a
        pn2.next = n1
        n1.next = b
    elif(j-i==1):
        pn1.next = n2
        n2.next = n1
        n1.next = b
    else:
        pn1.next = n2
        n2.next = a
        pn2.next = n1
        n1.next = b
     
    return head

head = takeInput()
head = swap(head,2,3)
printLL(head)