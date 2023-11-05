#Two Sum : Check if a pair with given sum exists in Array

def twoSum(arr,k):
    sortedArr = arr.sort()
    n = len(arr)
    i=0
    j=n-1
    while(i<j):
        if(arr[i]+arr[j]==k):
            print("{},{}".format(i,j))
            return "yes"
        elif(arr[i]+arr[j] < k):
            i+=1
        elif(arr[i]+arr[j] > k):
            j-=1
    print("-1,-1")
    return "no"

#using hashing
# def dup(arr,x):
#     ansDict={}
#     count=0
#     for i in range(len(arr)):
#         moreNeeded = x-arr[i]
#         if moreNeeded in ansDict:
#            count+=1
#            print("{}:{}".format(arr[i],moreNeeded))
#         ansDict[arr[i]]=i
#     return count
        
# arr = [2, 8, 10, 5, -2, 5]
# x=10

arr = [2,6,5,8,11]
k = 14
res = twoSum(arr,k)
print(res)