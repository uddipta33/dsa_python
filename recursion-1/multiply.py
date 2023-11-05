from audioop import mul


def multiply(n,m):
    if(n==0 or m==0):
        return 0
    smallOp = multiply(n,m-1)
    return n+smallOp

print(multiply(3,5))