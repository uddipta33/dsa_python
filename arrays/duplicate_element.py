def duplicate(array, n):
    i=0
    while(i<n-1):
        j=i+1
        while(j<n):
            if(array[i] == array[j]):
                return array[i]
            j+=1
        i+=1
    return -1

#better solution using hashing
# def dup(arr):
#     ansDict = {}
#     for i in range(len(arr)):
#         if arr[i] not in ansDict:
#             ansDict[arr[i]]=1
#         else:
#             ansDict[arr[i]]+=1
#     print(ansDict)
#     for k,v in ansDict.items():
#         if v>1:
#             return k
#             break


array = [0, 2, 1, 3, 1]
n = len(array)
res = duplicate(array,n)
print(res)