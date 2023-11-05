class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def takeInput():
    head = None
    tail = None
    newData = int(input())
    while(newData!=-1):
        newNode = Node(newData)
        if(head is None):
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = tail.next
        newData = int(input())
    return head

def printLL(head):
    ptr = head
    while(ptr!=None):
        print(ptr.data)
        ptr = ptr.next

def recLength(head):
    if(head is None):
        return 0
    smallOp = recLength(head.next)
    return smallOp+1

head = takeInput()
length = recLength(head)
print(length)