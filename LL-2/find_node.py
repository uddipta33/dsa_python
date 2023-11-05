from mymodule import *

def find(head,n):
    if(head is None):
        return -1
    if(head.data == n):
        return 0
    smallRes = find(head.next,n)
    if (smallRes==-1):
        return smallRes
    else:
        return smallRes + 1

head = takeInput()
res = find(head,60)
print(res)
