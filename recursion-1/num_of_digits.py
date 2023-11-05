def numDigits(n):
    if(n <= 9):
        return 1
    smallOp = numDigits(n/10)
    return 1 + smallOp

print(numDigits(31456))