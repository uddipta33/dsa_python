import re
from unittest import removeResult


def check(array,n):
    i=0
    for i in range(n-1):
        if(array[i]>array[i+1]):
            return i+1
    return 0

array = [1,2,3,4]
res = check(array,len(array))
print(res)