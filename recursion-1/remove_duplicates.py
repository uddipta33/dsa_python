#Given a string S, remove consecutive duplicates from it recursively.
def remove(input):
    if(len(input)<=1):
        return input
    
    smallOp = remove(input[1:])
    if(input[0]==input[1]):
        return smallOp
    else:
        return input[0]+smallOp

input = "aabccba"
print(remove(input))