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

def lengthLL(head):
    count=0
    if head is None:
        print("LL is empty")
    else:
        ptr = head
        while(ptr!=None):
            count+=1
            ptr=ptr.next
    return count 

def printLL(head):
    ptr = head
    while(ptr!=None):
        print(ptr.data)
        ptr = ptr.next