#Given an array and a sum k, we need to print the length of the longest subarray that sums to k.

#2 pointer solution (only for positive integers and zero)
def subarray(arr,k):
    i,j =0,0
    maxLen = 0
    sum=0
    n = len(arr)
    while(j<n):
        sum+=arr[j]
        if(sum==k):
            maxLen = max(maxLen, j-i+1)
            j+=1
        elif(sum>k):
            while(sum>k and i<=j):
                sum = sum - arr[i]
                i+=1
            if(sum == k):
                maxLen = max(maxLen, j-i+1)
            j+=1
        elif(sum<k):
            j+=1

    return maxLen

#for all postive,negative,zero
def subarrayBetter(arr, k):
    i=0
    maxLen = 0
    sum=0
    preSumMap = {} #hashmap using dict
    while(i<len(arr)):
        sum+=arr[i]
        if(sum==k):
            maxLen = max(maxLen, i+1)
        elif (sum-k) in preSumMap:
            maxLen = max(maxLen, i - preSumMap[sum-k])
        if(sum not in preSumMap):
            preSumMap[sum] = i
        i+=1
    return maxLen

# arr = [1,2,3,1,1,1,1,3,3]
arr = [2,0,0,3]
k=3
res = subarrayBetter(arr,k)
print(res)
