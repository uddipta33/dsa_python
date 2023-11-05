from array import array
from os import PRIO_USER


def binary_search(array,n,x):
    left = 0
    right = n-1
    while(left<=right):
        mid = (right+left)/2
        mid = int(mid)
        if (array[mid]==x):
            return mid
        if(x > mid):
            left = mid+1
        elif (x < mid):
            right = mid-1
    
    return -1

array = [2,4,5,7,9,10]
res=binary_search(array,len(array),11)
print(res)