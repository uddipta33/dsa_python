def partition(arr, si, ei):
    pivot = arr[si]
    count = 0 #counting no of elements smaller than pivot
    for i in range(si,len(arr)):
        if(arr[i] < pivot):
            count+=1
    pi = si+count
    temp = arr[pi]
    arr[pi] = pivot
    arr[si] = temp
    i = si
    j = ei
    while(i<pi and j>pi):
        if arr[i] < pivot:
            i+=1
        elif arr[j] >= pivot:
            j-=1
        else:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    return pi
        



def quickSort(arr, si, ei):
    if si < ei:
        pi = partition(arr, si, ei)
        quickSort(arr, si, pi-1)
        quickSort(arr, pi+1, ei)


input = [2, 6, 8, 5, 4, 3,1,7]
quickSort(input, 0, len(input)-1)
print(input)