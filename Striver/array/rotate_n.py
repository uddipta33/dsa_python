def reverse(a,s,e):
    i,j = s,e
    while(i<j):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        i+=1
        j-=1

def rotate(a,k):
    n = len(a)
    k=k%n # ik k > len(a)
    reverse(a,0,n-k-1)
    reverse(a,n-k,n-1)
    reverse(a,0,n-1)

a = [1,2,3,4,5,6,7]
k=2
rotate(a,k)
print(a)