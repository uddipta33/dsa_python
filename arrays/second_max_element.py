def sec(arr):
    maxi = max(arr[0],arr[1])
    sec_maxi = min(arr[0],arr[1])
    i=2
    while(i<len(arr)):
        if(arr[i]>maxi):
            sec_maxi = maxi
            maxi = arr[i]
        elif (arr[i]<maxi and arr[i]>sec_maxi):
            sec_maxi = arr[i]
        i+=1
    return sec_maxi

arr=[i for i in range(0,20,3)]
print(arr)
print(sec(arr))

            