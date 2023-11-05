def subsequence(input, output):
    if len(input)==0:
        output.append("")
        return 1
    
    smallOpSize = subsequence(input[1:], output)
    for i in range(0, smallOpSize):
        output.append(input[0]+output[i])
    
    return smallOpSize*2
'''
latest one
def sub(arr):
    if(len(arr)==0):
        return [""]
    smallOp = sub(arr[1:])
    for i in range(len(smallOp)):
        smallOp.append(arr[0]+smallOp[i])
    return smallOp

arr = "abc"
print(sub(arr))
'''

input = "abc"
output = []
size = subsequence(input,output)
print(output)