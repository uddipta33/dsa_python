def count_zeroes(n):
    if(n<=9):
        if(n==0):
            return 1
        else:
            return 0
    smallOp = count_zeroes(n//10)
    last = n%10
    if(last==0):
        return smallOp+1
    return smallOp

print(count_zeroes(00))