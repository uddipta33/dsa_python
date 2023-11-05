#hashing - O(n)
def removeDup(arr):
    mydict = {}
    op = []
    for i in range(len(arr)):
        if arr[i] in mydict:
            continue
        mydict[arr[i]] = 1
        op.append(arr[i])
    return op
    
arr = [1,2,3,3,5,5,5,8,8,7]
res = removeDup(arr)
print(res)