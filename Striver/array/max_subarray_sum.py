#Given an integer array arr, find the contiguous subarray (containing at least one number) which
#has the largest sum and returns its sum and prints the subarray.
import sys
#brute-force solution
def maxSum(arr):
    n = len(arr)
    maxSum=arr[0]
    for i in range(n):
        sum = 0
        for j in range(i,n):
            sum+=arr[j]
            maxSum = max(maxSum,sum)
    return maxSum

#Kadane's algo - O(n)
def kadane(arr):
    sum=0
    maxi = arr[0]
    for i in range(len(arr)):
        sum+=arr[i]
        maxi = max(maxi,sum)
        if(sum<0):
            sum=0
    return maxi

arr = [-2,1-3,4,-1,2,1,-5,4]
# res = kadane(arr)
res = maxSum(arr)
print(res)
