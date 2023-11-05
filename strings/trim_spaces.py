from itertools import count
import re


def trim(line,n):
    ans = ""
    i,j=0,0
    while(i<n):
        if line[i]!=" ":
            ans = ans + line[i]
        i+=1
    return ans

line= "abc def g hi zj"
res = trim(line,len(line))
print(res)