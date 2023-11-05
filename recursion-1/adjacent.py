import re


def adjacent(input):
    if(len(input)==1):
        return input
    smallOp = adjacent(input[1:])
    if (input[0]==input[1]):
        res = input[0] + "*" + smallOp
        return res
    return input[0]+smallOp

res = adjacent("aacdd")
print(res)