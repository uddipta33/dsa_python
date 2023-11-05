#Given an array, print all the elements which are leaders. A Leader is an element that is greater than all of the elements on its right side in the array.

#brute-force 
def leader(arr):
    n = len(arr)
    for i in range(n-1):
        j=i+1
        while(j<n):
        #for j in range(i+1,n):
            if(arr[j]>arr[i]):
                break
            j+=1
        if(j==n):
            print(arr[i])
    print(arr[n-1])

#optimal method
def leaderOptimal(arr):
    n = len(arr)
    i = n-2
    maxi = arr[n-1]
    print(arr[n-1]) #last element is always a leader
    while(i>=0):
        if(arr[i] > maxi):
            maxi = arr[i]
            print(arr[i])
        i-=1

        

#arr = [4, 7, 1, 0]
arr = [10, 22, 12, 3, 0, 6]
leaderOptimal(arr)
