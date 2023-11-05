'''
   *
  **
 ***
**** 
'''
n = int(input("enter no of rows -- "))
i=1
while(i<=n):
    # for spaces
    j = 1
    while(j<=(n-i)):
        print(" ", end="")
        j+=1
    # for stars
    j=1
    while(j<=i):
        print("*", end="")
        j+=1
    print('\r')
    i+=1

