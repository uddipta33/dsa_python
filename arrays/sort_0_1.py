from array import array
from operator import le


def sort01(array, n):
    i=0
    nextZero = 0
    for i in range(n):
        if array[i]==0:
            tmp = array[i]
            array[i] = array[nextZero]
            array[nextZero] = tmp
            nextZero+=1

array = [0, 1, 1, 0, 1, 0, 1]
n = len(array)
sort01(array,n)
print(array)