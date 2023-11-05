from mymodule import *

def arrange(head):
    if(head is None or head.next== None):
        return head
    
    eh = None
    et = None
    oh = None
    ot = None
    ptr = head
    while(ptr!=None):
        if(ptr.data%2==0):
            if(eh==None):
                eh=ptr
                et = ptr
                ptr = ptr.next
            else:
                et.next = ptr
                et = ptr
                ptr = ptr.next
        else:
            if(oh==None):
                oh = ptr
                ot = ptr
                ptr = ptr.next
            else:
                ot.next = ptr
                ot = ptr
                ptr = ptr.next
    if(oh==None):
        return eh
    elif(eh==None):
        return oh
    else:
        ot.next = None
        et.next = None
        ot.next = eh
        return oh

head = takeInput()
head = arrange(head)
printLL(head)