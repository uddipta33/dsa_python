# You have been given an integer array/list(ARR) of size N. Where N is equal to [2M + 1].
# Now, in the given array/list, 'M' numbers are present twice and one number is present only once.
# You need to find and return that number which is unique in the array/list.

def unique(array, n):
    i = 0
    
    while(i<n):
        if (array[i]!= -1):
            j = i+1
            while(j<n):
                if(array[i]==array[j]):
                    array[j] = -1
                    break
                j+=1
                
            if(j>=n):
                return array[i]
        i+=1

#better technique (since a ^ a = 0)
# def unique(arr):
#     res = 0
#     for i in range(len(arr)):
#         res = res ^ arr[i]
#     return res



array = [2, 4, 7, 2, 7]
n = len(array)
res = unique(array,n)
print(res)




