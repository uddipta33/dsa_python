def second_largest(array,n):
    if(len(array) <2):
        return -1
    largest = max(array[0],array[1])
    second_lar = min(array[0],array[1])

    for i in range(2,n):
        if array[i] > largest:
            second_lar = largest
            largest = array[i]
        elif array[i] > second_lar and array[i]!=largest:
            second_lar = array[i]
    return second_lar

array = [4,3]
res = second_largest(array, len(array))
print(res)