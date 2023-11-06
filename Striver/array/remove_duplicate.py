def remove_dup(a):
    n = len(a)
    i=0
    for j in range(1,n):
        if(a[i]!=a[j]):
            i+=1
            a[i] = a[j]
    return i+1 

a= [1,1,2,2,2,3,3]
size = remove_dup(a)
for i in range(0,size):
    print(a[i])