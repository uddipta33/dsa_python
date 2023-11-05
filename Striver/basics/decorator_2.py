def smart_divide(func):
    def inner(a,b):
        print("Dividing ",a ," by ", b)
        if b==0:
            print("Cannot divide by 0")
            return
        else:
            return func(a,b)
    return inner

# @smart_divide
def divide(a,b):
    return a/b

res_func = smart_divide(divide)
res = res_func(20,4)
print(res)


# res = divide(20,4)
# print(res)