'''
1
2 2
3 3 3
4 4 4 4
'''
n = int(input("enter no of rows -- "))
i=1
while(i<=n):
    j=1 
    while(j<=i):
        print(i, end=" ")
        j+=1
    print('\r')
    i+=1

