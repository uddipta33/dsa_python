#left rotate by one place
def rotate(a):
    n = len(a)
    temp = a[0]
    for i in range(1,n):
        a[i-1] = a[i]
    a[n-1] = temp

a = [1,2,3,4,5]
rotate(a)
print(a)