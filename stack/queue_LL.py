class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class QueueUsingLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def getSize(self):
        return self.size
    
    def enqueue(self, element):
        n1 = Node(element)
        if(self.head is None):
            self.head = n1
            self.tail = n1
        else:
            self.tail.next = n1
            self.tail = n1
        self.size+=1
    
    def front(self):
        if(self.head is None):
            print("Queue is empty")
            return
        else:
            return self.head.data
    
    def dequeue(self):
        if(self.head is None):
            print("Queue is empty")
            return
        else:
            ans = self.head.data
            self.head = self.head.next
            self.size-=1
            return ans
    
    def isEmpty(self):
        return self.size==0