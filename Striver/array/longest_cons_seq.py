#brute-force
# def ls(a,x):
#     n = len(a)
#     for i in range(0,n):
#         if a[i]==x:
#             return True
#     return False

# def lonseq(a):
#     n = len(a)
#     maxi = 0
#     count = 0
#     for i in range(0,n):
#         count = 1
#         x = a[i]+1
#         while ls(a,x):
#             x+=1
#             count+=1
#         maxi = max(maxi,count)
#     return maxi


def better(a):
    n = len(a)
    lastSmall = -100000
    currCount = 0
    maxi = 0
    a.sort()
    for i in range(0,n):
        if(a[i]-1 == lastSmall):
            currCount+=1
            lastSmall=a[i]
        elif(a[i]-1 != lastSmall):
            currCount = 1
            lastSmall = a[i]
        maxi = max(currCount,maxi)
    return maxi

#optimal using set
def optimal(a):
    n = len(a)
    st = set()
    for i in a:
        st.add(i)
    maxi = 0
    for i in st:
        count=1
        if(i-1 in st):
            break
        x = i+1
        while(x in st):
            count+=1
            x+=1
        maxi = max(maxi,count)
    return maxi

arr = [100, 200, 1, 3, 2, 4]
res = optimal(arr)
print(res) 