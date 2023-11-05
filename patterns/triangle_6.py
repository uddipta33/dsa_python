'''
A A A A
B B B B
C C C C
D D D D
'''
n = int(input("enter no of rows -- "))
i=1
p=1
while(i<=n):
    j=1 
    while(j<=n):
        ch  = chr(ord('A')+ i-1)
        print(ch, end=" ")
        j+=1
    print('\r')
    i+=1

