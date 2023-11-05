from array import array


def pair_sum(array,n,x):
    pairs = 0
    for i in range(0,n-1):
        for j in range(i+1,n):
            if array[i]+array[j] == x:
                pairs+=1
        
    return pairs

array=[1, 3, 6, 2, 5, 4, 3, 2, 4]
x=7
n=len(array)
res = pair_sum(array,n,x)
print(res)