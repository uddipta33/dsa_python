

def longest(arr):
    arr.sort()
    count=0
    maxi = 0
    n = len(arr)
    for i in range(n-1):
        if(arr[i+1]-arr[i]==1):
            count+=1
            maxi = max(maxi,count)
    return maxi+1

arr = [100, 200, 1, 3, 2, 4]
res = longest(arr)
print(res) 