#print pascal triangle



def nth_row(n):
    ans = 1
    ansList = [1]
    for i in range(1,n):
        ans = ans * (n-i)
        ans = ans//i
        ansList.append(ans)
    return ansList

def pascal(rows):
    mainList = []
    for i in range(1,rows+1): 
        mainList.append(nth_row(i))
    return mainList

rows = int(input("Enter the no. of rows  : "))
res = pascal(rows)
print(res)