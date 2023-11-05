'''
1
2 1
3 2 1
4 3 2 1
'''
n = int(input("enter no of rows -- "))
i=1
while(i<=n):
    j=1
    p=i
    while(j<=i):
        print(p, end=" ")
        p-=1
        j+=1
    print('\r')
    i+=1

