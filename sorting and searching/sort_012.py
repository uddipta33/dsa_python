def sort_012(a,n):
    i,nz,nt = 0,0,n-1
    while(i<=nt):
        if(a[i]==0):
            temp = a[i]
            a[i] = a[nz]
            a[nz] = temp
            i+=1
            nz+=1
        elif a[i]==2:
            temp = a[i]
            a[i] = a[nt]
            a[nt] = temp
            nt-=1
        else:
            i+=1

a = [0, 1, 2, 0, 2, 0, 1]
sort_012(a,len(a))
print(a)
