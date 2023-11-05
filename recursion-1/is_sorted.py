import re


def is_sorted(arr, n):
    if(n==0 or n==1):
        return True
    
    if( arr[0] > arr[1]):
        return False
    
    smallOp = is_sorted(arr[1:], n-1)
    return smallOp

arr= [1,3,4,5,2]
print(is_sorted(arr,len(arr)))
