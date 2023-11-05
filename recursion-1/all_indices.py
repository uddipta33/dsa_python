def all_indices(input,n,x,output):
    if(n==0):
        return 0
    
    smallOp = all_indices(input,n-1, x, output)
    if input[n-1]==x:
        output.append(n-1)
        return smallOp+1
    else:
        return smallOp

input = [9, 8, 10, 8, 8]
output=[]
print(all_indices(input,len(input),10,output))
print(output)