#filter(function , iterable)
arr = [1,2,3,4,5]
res = list(filter(lambda x : x%2==0, arr))
print(res)