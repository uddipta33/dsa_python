from cgitb import small
import re


def binary_search(arr, si, ei, x):
    if(si>ei):
        return -1
    mid = (si+ei)//2
    if(arr[mid]==x):
        return mid
    elif (x<arr[mid]):
        smallOp = binary_search(arr, si, mid-1, x)
        return smallOp
    else:
        smallOp = binary_search(arr, mid+1, ei, x)
        return smallOp

arr = [2, 3, 4, 5, 6, 8]
last = len(arr)-1
res = binary_search(arr, 0, last, 5)
print(res)
