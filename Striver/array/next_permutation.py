def per(a):
    n = len(a)
    idx = -1
    i=n-2
    while(i>=0):
        if(a[i]<a[i+1]):
            idx = i
            break
        i-=1
    if(idx==-1):
        a.reverse()
        return a
    i=n-1
    while(i>idx):
        if(a[i]>a[idx]):
            temp = a[idx]
            a[idx] = a[i]
            a[i] = temp
            break
        i-=1
    a[idx+1:] = reversed(a[idx+1:])
    return a

a = [1,3,2]
res = per(a)
print(res)