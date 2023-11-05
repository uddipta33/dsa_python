def palindrome(line,n):
    i,j = 0,n-1
    flag = 1
    while(i<j):
        if(line[i] == line[j]):
            i+=1
            j-=1
        else:
            flag=0
            return flag
    
    return flag

line="malayala"
flag = palindrome(line,len(line))
print(flag)