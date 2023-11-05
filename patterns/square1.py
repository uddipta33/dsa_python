'''
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4
'''

def pattern(n):
    i = 1
    while(i <= n):
        j = 1
        while(j <= n):
            print(j, end=" ")
            j+=1
        i+=1
        print('\r')
    

rows = int(input("Enter no. of rows... "))
pattern(rows)
