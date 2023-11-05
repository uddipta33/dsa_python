from mainfile import *

def midLL(head):
    if (head is None):
        return
    fast = head.next
    slow = head
    while(fast!=None and fast.next!=None):
        slow=slow.next
        fast = fast.next.next 
    return slow.data
head = takeInput()
res = midLL(head)
print(res)
