#Union of Two Sorted Arrays

def union(a1,a2):
    n = len(a1)
    m = len(a2)
    ansDict = {}
    for i in range(0,n):
        if a1[i] not in ansDict:
            ansDict[a1[i]] = 1
    
    for j in range(0,m):
        if a2[j] not in ansDict:
            ansDict[a2[j]] = 1
    res= []
    for k,v in ansDict.items():
        res.append(k)
    return res


a1 = [1,2,3,4,5,6,7,8,9,10]
a2 = [2,3,4,4,5,11,12]
res = union(a1,a2)
print(res)