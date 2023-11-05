def printNum(n):
    if(n==0):
        return
    printNum(n-1)
    print(n)

printNum(0)