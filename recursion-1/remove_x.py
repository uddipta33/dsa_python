def remove(input):
    if(len(input)==0):
        return input
    smallOp = remove(input[1:])
    if(input[0]=='x'):
        return smallOp
    return input[0]+smallOp


input='xxabxb'
print(remove(input))
    
    