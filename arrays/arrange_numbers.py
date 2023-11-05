def arrange(array, n):
    left = 0
    right = n-1
    num = 1
    while(left<=right):
        if num%2 == 1:
            array[left] = num
            num+=1
            left+=1
        else:
            array[right] = num
            num+=1
            right-=1
        

n = 7
array = n * [0]

arrange(array,n)
print(array)