def push_zeroes(array,n):
    i = 0
    k=0
    while(i<n):
        if(array[i]==0):
            i+=1
        else:
            temp = array[k]
            array[k] = array[i]
            array[i] = temp
            k+=1
            i+=1

array = [0,0,0,1,3,0,0]
push_zeroes(array,len(array))
print(array) 