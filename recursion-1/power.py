def power(x,n):
    if(n == 0):
        return 1
    smallOp = power(x,n-1)
    return x*smallOp

res = power(2,5)
print(res)