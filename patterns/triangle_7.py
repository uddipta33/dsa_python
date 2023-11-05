'''
A B C D
A B C D
A B C D
A B C D
'''
n = int(input("enter no of rows -- "))
i=1
while(i<=n):
    j=1 
    while(j<=n):
        ch  = chr(ord('A')+ j-1)
        print(ch, end=" ")
        j+=1
    print('\r')
    i+=1

