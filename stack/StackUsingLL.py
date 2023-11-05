class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class StackUsingLL:
    def __init__(self):
        self.head = None
        self.size = 0
    
    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size==0
    
    def push(self,element):
        n1 = Node(element)
        if(self.head is None):
            self.head = n1
        else:
            n1.next = self.head
            self.head = n1
        self.size+=1
    
    def pop(self):
        if(self.head is None):
            print("Stack is empty")
            return
        temp = self.head.data
        self.head = self.head.next
        self.size-=1
        return temp
    
    def top(self):
        if(self.head is None):
            print("Stack is empty")
            return
        return self.head.data

# s1 = StackUsingLL()
# s1.push(10)
# s1.push(20)
# s1.push(30)
# s1.push(40)
# print(s1.pop())
# print(s1.pop())
# print(s1.top())
# print(s1.isEmpty())


    