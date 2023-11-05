#You are given an array of prices where prices[i] is the price of a given stock on an ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

#brute-force solution

def stock(arr):
    maxPro=0
    n = len(arr)
    for i in range(n-1):
        profit = 0
        for j in range(i+1,n):
            profit = arr[j] - arr[i]
            maxPro = max(maxPro,profit)
    return maxPro

#optimal solution
def stockOptimal(arr):
    maxPro = 0
    minPrice = arr[0]
    profit = 0
    for i in range(len(arr)):
        minPrice = min(minPrice,arr[i])
        profit = arr[i] - minPrice
        maxPro = max(maxPro, profit)
    return maxPro

arr = [7,1,5,3,6,4]
res = stockOptimal(arr)
print(res)
