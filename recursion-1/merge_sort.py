# def merge(input, s, mid, e):
#     print(input)
#     b=[]
#     i,j = s,mid+1
#     while(i<=mid and j<=e):
#         if(input[i] < input[j]):
#             b.append(input[i])
#             i+=1
#         else:
#             b.append(input[j])    
#             j+=1
#     while(i<=mid):
#         b.append(input[i])
#         i+=1
#     while(j<=e):
#         b.append(input[j])
#         j+=1
#     print(b)
#     for i in range(0,len(input)):
#         input[i] = b[i]

def merge(input, s, mid, e):
    num1 = mid-s+1
    num2 = e-mid
    #left subarray
    L = [0] * num1
    #right subarray
    R = [0] * num2
    
    for i in range(0,num1):
        L[i] = input[s+i]
    for j in range(0,num2):
        R[j] = input[mid+j+1]
    
    i=0
    j=0
    k=s
    while(i < num1 and j<num2):
        if(L[i] < R[j]):
            input[k] = L[i]
            i+=1
            k+=1
        else:
            input[k] = R[j]
            j+=1
            k+=1
    while(i<num1):
        input[k] = L[i]
        i+=1
        k+=1
    while(j<num2):
        input[k] = R[j]
        j+=1
        k+=1

def merge_sort(input,s,e):
    if(s<e):
        mid = (s+e) // 2
        merge_sort(input, s, mid)
        merge_sort(input, mid+1, e)
        merge(input, s, mid, e)

input = [2, 13, 4, 1, 3, 6, 28]
last = len(input)-1
merge_sort(input, 0, last)
print(input)
