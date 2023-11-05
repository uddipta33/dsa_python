class stackUsingArray:
    def __init__(self, totalsize):
        self.data = [0]*totalsize
        self.nextIndex = 0
        self.capacity = totalsize
    
    def size(self):
        return self.nextIndex
    
    def isEmpty(self):
        return self.nextIndex == 0
    
    def push(self, element):
        if(self.nextIndex == self.capacity):
            print("Stack is full")
            return
        else:
            self.data[self.nextIndex] = element
            self.nextIndex+=1

    def pop(self):
        if(self.isEmpty()):
            print("Stack is empty")
            return -1
        self.nextIndex-=1
        return self.data[self.nextIndex]
    
    def top(self):
        if(self.isEmpty()):
            print("Stack is empty")
            return -1
        return self.data[self.nextIndex-1]
