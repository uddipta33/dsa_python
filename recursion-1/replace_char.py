from cgitb import small


def replace(input, c1, c2):
    if(len(input)==0):
        return input
    smallOp = replace(input[1:],c1,c2)
    if(input[0]==c1):
        return c2 + smallOp
    else:
        return input[0]+smallOp

input = "abacdaaaa"
print(replace(input,'a','x'))    