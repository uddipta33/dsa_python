#There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements. Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.



def rearrange(arr):
    
    n=len(arr)
    op=[0]*n
    posIndex = 0
    negIndex=1
    for i in range(len(arr)):
        if(arr[i]>0):
            op[posIndex]=arr[i]
            posIndex+=2
        if(arr[i]<0):
            op[negIndex] = arr[i]
            negIndex+=2
    return op

arr=[1,2,-3,-1,-2,3]
res = rearrange(arr)
print(res)