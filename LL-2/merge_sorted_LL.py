from mymodule import *

def merge(h1, h2):
    print("h1.data",h1.data)
    print("h2.data",h2.data)
    fh = None
    ft = None
    if(h1.data < h2.data):
        fh = h1
        ft = h1
        h1 = h1.next
    else:
        fh = h2
        ft = h2
        h2 = h2.next
    while(h1!=None or h2!=None):
        if(h1.data < h2.data):
            ft.next = h1
            ft = h1
            h1 = h1.next
        else:
            ft.next = h2
            ft = h2 
            h2 = h2.next 
    while(h1!=None):
        ft.next = h1
        ft = h1
        h1 = h1.next
    while(h2!=None):
        ft.next = h2
        ft = h2
        h2 =h2.next
    return fh 

h1 = takeInput()
# print("h1.data",h1.data)
h2 = takeInput()
# print("h2.data",h2.data)
# print(h1.data < h2.data)
fh = merge(h1,h2)
printLL(fh)