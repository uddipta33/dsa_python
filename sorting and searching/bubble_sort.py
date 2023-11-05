from array import array


def bubble_sort(array,n):
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


array= [10,1,7,9,14,5]
bubble_sort(array,len(array))
print(array)