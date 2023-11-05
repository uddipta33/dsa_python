'''
1
2 3
3 4 5
4 5 6 7
'''
n = int(input("enter no of rows -- "))
i=1
while(i<=n):
    j=1 
    p=i
    while(j<=i):
        print(p, end=" ")
        p+=1
        j+=1
    print('\r')
    i+=1

