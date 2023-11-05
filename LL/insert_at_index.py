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

def insert(head,i,data):
    ptr = head
    count=0
    if(i==0):
        newNode = Node(data)
        newNode.next = head
        head = newNode
        return head
    while(ptr!=None and count < i-1):
        ptr = ptr.next
        count+=1
    if( ptr!=None):
        newNode = Node(data)
        newNode.next = ptr.next
        ptr.next = newNode
    return head    

def delete(head,i):
    if(i==0):
        ptr = head
        head = head.next
        ptr.next = None
        return head
    count=0
    ptr = head
    while(ptr.next!=None and count<i-1):
        ptr = ptr.next
        count+=1
    if(ptr.next!=None):
        a = ptr.next
        ptr.next = a.next
        a.next = None
        return head

#####
head = takeInput()
#head = insert(head,0,99)
head = delete(head,2)
printLL(head)
