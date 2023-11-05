from mymodule import *

def mid(head):
    if(head is None):
        return -1
    slow = head
    fast = head.next
    length = lengthLL(head)
    if(length%2==0):
        while(fast.next!=None):
            slow = slow.next
            fast = fast.next.next
        return slow.data
    else:
        while(fast!=None):
            slow = slow.next
            fast = fast.next.next
        return slow.data

head = takeInput()
num = mid(head)
print(num)