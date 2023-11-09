#Find the Majority Element that occurs more than N/2 times

#2nd best solution using hashing
def majority(arr):
    dictMap = {}
    i=0
    n = len(arr)
    while(i<n):
        if(arr[i] not in dictMap):
            dictMap[arr[i]]=1
        elif( arr[i] in dictMap):
            dictMap[arr[i]]+=1
        i+=1
    for num,val in dictMap.items():
        if (val > n//2):
            return num
    return -1 

#optimal (Moore's voting algo)
# def majorityElement(nums) -> int:
#         el = None
#         count = 0
#         n = len(nums)
#         for i in range(0,n):
#             if(count==0):
#                 el = nums[i]
#                 count=1
#             elif(nums[i] == el):
#                 count+=1
#             else:
#                 count-=1
#         return el


arr = [4,4,2,4,3,4,4,3,2,4]
res = majority(arr)
print(res)