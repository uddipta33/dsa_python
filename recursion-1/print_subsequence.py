def sub(input, op):
    if(len(input)==0):
        print(op)
        return
    sub(input[1:],op)
    sub(input[1:], op+input[0])

input = "abc"
op=""
sub(input,op)