from StackUsingLL import *
s1 = StackUsingLL()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)

s2 = StackUsingLL()
while(not s1.isEmpty()):
    top = s1.top()
    s2.push(top)
    s1.pop()

while not s2.isEmpty():
    print(s2.pop())
