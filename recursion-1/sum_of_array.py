def sum(arr, n):
    if(n==0):
        return 0
    smallOp = sum(arr[1:], n-1)
    return arr[0] + smallOp

arr = [1,4,5,8]
print(sum(arr,len(arr)))