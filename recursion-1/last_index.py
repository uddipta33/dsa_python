import re


def last_index(arr, n, x):
    if(n==0):
        return -1
    smallOp = last_index(arr[1:],n-1,x)
    if (smallOp == -1):
        if (arr[0]==x):
            return 0
        else:
            return -1
    else: 
        return smallOp+1

arr=[9, 8, 10, 8]
print(last_index(arr,len(arr),1))    