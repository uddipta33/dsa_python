def check(arr,n, x):
    if(n==0):
        return False
    
    smallOp = check(arr[1:],n-1,x)
    if(smallOp):
        return True
    else:
        if(arr[0]==x):
            return True
        else:
            return False

arr = [2,3,4,7]
print(check(arr,len(arr),2))