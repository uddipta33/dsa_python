'''
A
BB
CCC
'''
n = int(input("enter no of rows -- "))
i=1
while(i<=n):
    j=1 
    while(j<=i):
        ch  = chr(ord('A')+ i-1)
        print(ch, end=" ")
        j+=1
    print('\r')
    i+=1

