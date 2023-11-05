def reverse(a,n):
    i,j=0,n-1
    ans1 = ""
    while(j>=0):
        ans1 = ans1 + a[j]
        j-=1
    # print(ans1)
    i=0
    start = 0
    ans = ""
    for i in range(n):
        if(ans1[i]==" "):
            j=i-1
            while(j>=start):
                ans = ans+ ans1[j]
                j-=1
            ans = ans + " "
            start = i+1
        elif i == n-1:
            j=i
            while(j>=start):
                ans = ans+ ans1[j]
                j-=1
    return ans
            



line = "come here again"
print(reverse(line,len(line)))