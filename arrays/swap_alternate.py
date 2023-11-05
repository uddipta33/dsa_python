def swap(array, n):
    i=0
    while(i<n-1):
        tmp = array[i]
        array[i] = array[i+1]
        array[i+1] = tmp
        i+=2

array = [5,8,9,7,3,4,19]
n = len(array)
swap(array,n)
print(array)