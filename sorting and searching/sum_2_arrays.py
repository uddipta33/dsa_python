def sum(a1,n1,a2,n2,a3):
    n3 = max(n1,n2) + 1
    carry=0
    i,j,k =n1-1,n2-1,n3-1
    while(i>=0 and j>=0):
        res = a1[i] + a2[j] + carry
        reqd = res%10
        carry = int(res/10)
        a3[k] = reqd
        i-=1
        j-=1
        k-=1
    while(i>=0):
        res = a1[i] + carry
        reqd = res%10
        carry = int(res/10)
        a3[k]=reqd 
        i-=1
        k-=1
    while(j>=0):
        res = a2[j] + carry
        reqd = res%10
        carry = int(res/10)
        a3[k]=reqd 
        j-=1
        k-=1
    if carry!=0:
        a3[k] = carry
    
a1 = [6, 2, 4]
a2=[7, 5, 6]
size3 = max(len(a1),len(a2)) +1
a3 = [0] * size3
sum(a1,len(a1),a2,len(a2),a3)
print(a3)
    