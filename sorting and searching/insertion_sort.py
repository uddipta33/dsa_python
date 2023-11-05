from array import array


def insertion_sort(array,n):
    for i in range(1,n):
        current = array[i]
        j=i-1
        while(j>=0):
            if(current < array[j]):
                array[j+1] = array[j]
                j-=1
            else:
                break
        array[j+1] = current

array = [10,5,3,15,4]
insertion_sort(array,len(array))
print(array)
        