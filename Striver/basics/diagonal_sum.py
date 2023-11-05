def diagSum(arr,n,m):
    sum=0
    # for i in range(n):
    #     for j in range(m):
    #         if(i==j):
    #             sum = sum + arr[i][j]
    #             break
    # return sum
    for i in range(n):
        for j in range(m):
            if(j==(n-i-1)):
                sum = sum + arr[i][j]
                break
    return sum

arr = [[2,5,6,8],[7,2,8,5],[3,7,5,4],[5,6,4,8]]
res = diagSum(arr,4,4)
print(res)
