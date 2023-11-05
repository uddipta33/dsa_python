from array import array


def selection_sort(array,n):
    i=0
    for i in range(0,n-1):
        min = array[i]
        minIndex = i
        
        for j in range(i+1,n):
            if (array[j] < min):
                min = array[j]
                minIndex = j
        temp = array[i]
        array[i] = min
        array[minIndex] = temp
    

array = [10,1,6,9,0,4]
selection_sort(array, len(array))
print(array)