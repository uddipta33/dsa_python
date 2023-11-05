def printKeypad(num,op):
    if(num==0):
        print(op)
        return
    last = num%10
    mapping = ["","","abc","def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    reqdString = mapping[last]
    for i in range(len(reqdString)):
        printKeypad(num//10, reqdString[i]+op)

num = 23
op = ""
printKeypad(num,op)
        