'''
A
B C
C D E
D E F G
'''
n = int(input("enter no of rows -- "))
i=1
while(i<=n):
    j=1
    p=i
    while(j<=i):
        ch  = chr(ord('A')+ p-1)
        print(ch, end=" ")
        p+=1
        j+=1
    print('\r')
    i+=1

