'''
A B C D
B C D E
C D E F
D E F G
'''
n = int(input("enter no of rows -- "))
i=1
while(i<=n):
    j=1 
    while(j<=n):
        ch  = chr((ord('A')+ i-1) + (j-1))
        print(ch, end=" ")
        j+=1
    print('\r')
    i+=1

