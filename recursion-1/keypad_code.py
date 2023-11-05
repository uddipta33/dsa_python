#return keypad code (not done)
def keypad(num):
    if(num==0):
        return [""]
    smallOp = keypad(num//10)
    last = num%10
    mapping = ["","","abc","def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    reqdRes = mapping[last]
    length = len(reqdRes)
    smallOpLen = len(smallOp)
    smallOp = smallOp*length
    k=0
    for i in range(length):
        for j in range(smallOpLen):
            smallOp[k] = smallOp[k] + reqdRes[i]
            k+=1
    return smallOp
    
num = 23
op = keypad(num)
print(op)

    