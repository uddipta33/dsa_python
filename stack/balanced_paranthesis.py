from StackUsingLL import *

def checkBalance(line):
    s1 = StackUsingLL()
    for i in line:
        if(i=='('):
            s1.push(i)
        elif(i==')'):
            if (s1.isEmpty()):
                return False
            if(s1.top()=='('):
                s1.pop()
            else:
                return False
    
    if(s1.isEmpty()):
        return True
    else:
        return False

line = "()()(()"
res = checkBalance(line)
print(res)
