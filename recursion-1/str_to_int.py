def change(input):
    if(len(input)==1):
        return ord(input)-48
    
    smallOp = change(input[1:])
    last = ord(input[0])-48
    res = ( last * (10**(len(input)-1)) ) + smallOp
    return res

res = change("3456")
print(res)
print(type(res))