class Node:
   def __init__(self, data):
       self.data = data
       self.next = None

def takeInput():
    head = None
    tail = None
    newData = int(input())
    while newData!= -1:
        newNode = Node(newData)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = tail.next
        newData = int(input())
    return head

def printLL(head):
    if head is None:
        return
    tmp = head
    while(tmp!=None):
        print(tmp.data)
        tmp = tmp.next 

def lengthLL(head):
    if head is None:
        return 0
    ptr = head
    count = 0
    while(ptr is not None):
        count+=1
        ptr = ptr.next 
    return count

def printAtIndex(head ,i):
    if(i>=lengthLL(head)):
        return -1
    count = 0
    ptr = head
    while(count!=i):
        
        count+=1
        ptr = ptr.next 
    print(ptr.data)

# head = takeInput()
# printLL(head)
# print(lengthLL(head))
# printAtIndex(head, 2)    