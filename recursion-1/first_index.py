def first_index(arr,n,x):
    if(n==0):
        return -1
    if (arr[0]==x):
        return 0
    smallOp = first_index(arr[1:], n-1,x)
    if smallOp == -1:
        return smallOp
    else:
        return 1+smallOp
    

arr=[5,5,6,6,7,8]
print(first_index(arr,len(arr),7))