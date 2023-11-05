

def subset(arr):
    if (len(arr)==0):
        output = [[]]
        return output
    
    output = subset(arr[:len(arr)-1])
    outputLen = len(output)
    # print(smallOp)
    last = arr[len(arr)-1]

    for i in range(0,outputLen):
        output.append(output[i].copy())
        # output[len(smallOp)+i].append(last)
        output[outputLen+i].append(last)
    # return output
    return output
arr = [15,20,12]
op = subset(arr)
print(op)