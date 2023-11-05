'''
1
12
123
1234
'''
n = int(input("enter no of rows -- "))
i=1
while(i<=n):
    j=1
    while(j<=i):
        print(j, end=" ")
        j+=1
    print('\r')
    i+=1

