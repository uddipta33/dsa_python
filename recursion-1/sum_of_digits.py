def sum(n):
    if(n<=9):
        return n
    smallOp = sum(n//10)
    last = n%10
    return last+smallOp

print(sum(978))