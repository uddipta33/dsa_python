'''
1234
123
12
1
'''
n = int(input("enter no of rows -- "))
i=1
while(i<=n):
    j = 1
    while(j<=(n-i+1)):
        print(j, end="")
        j+=1
    
    print('\r')
    i+=1

