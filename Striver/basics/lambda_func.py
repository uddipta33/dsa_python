#lambda arguments : expression

def mul(arr):
    return [i*2 for i in arr]

arr= [15,50,35,9]
ans =  lambda x : [i for i in arr if i>20]
print(ans(arr)) 