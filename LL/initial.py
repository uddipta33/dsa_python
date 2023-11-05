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

def printAtIndex(head,i):
    length = lengthLL(head)
    if(i>length):
        return
    ptr = head
    index = 0
    while(ptr!=None):
        if(i==index):
            print(ptr.data)
            return
        index+=1
        ptr = ptr.next

head = takeInput()
printLL(head)
length = lengthLL(head)
print(length)
printAtIndex(head,3)

# head = None
# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)
# n1.next = n2
# n2.next = n3
# head = n1
# ptr = head
# while(ptr != None):
#     print(ptr.data)
#     ptr = ptr.next