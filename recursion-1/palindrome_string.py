from cgitb import small


def palindrome(line):
    length = len(line)
    if(length<=1):
        return True
    if(line[0] != line[length-1]):
        return False
    smallOp = palindrome(line[1:-1])
    return smallOp

line = "malayala"
print(palindrome(line))