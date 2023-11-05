#Given an array A of size n and an integer K, return all subsets of A which sum to K.
#Return subsets sum to K
def sum(input,k):
    if(len(input)==0):
        if k==0:
            return [[]]
        else:
            return []
    op1 = sum(input[1:], k)
    op2 = sum(input[1:], k-input[0])
    for i in range(len(op2)):
        op2[i] = [input[0]] + op2[i]
    size = len(op1)+len(op2)
    b = [0] *size
    k=0
    for i in range(len(op1)):
        b[k] = op1[i]
        k+=1
    for i in range(len(op2)):
        b[k] = op2[i]
        k+=1

    return b

input = [5, 12, 3, 17, 1, 18, 15, 3, 17 ]
k=6
res = sum(input,k)
print(res)    