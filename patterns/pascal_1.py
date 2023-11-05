def ncr(r,c):
    res = 1
    for i in range(0,c):
        res= res * (r-i)
        res = res//(i+1)
    return res

r = int(input("enter the row no. "))
c = int(input("enter the column no. "))
res = ncr(r-1,c-1)
print(res)