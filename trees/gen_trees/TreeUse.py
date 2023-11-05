from TreeNodeClass import *

def printTree(root):
    if(root is None):
        return
    
    print(root.data, end=": ")

    for i in range(len(root.children)):
        print(root.children[i].data, end=" ")
    print("\n")
    for i in range(len(root.children)):
        printTree(root.children[i])

def takeInput():
    rootData = int(input("enter data : "))
    root = TreeNode(rootData)
    numChild = int(input("Enter no. of children of {} : ".format(root.data)))
    for i in range(numChild):
       child = takeInput()
       root.children.append(child)
    
    return root



# root = TreeNode(1)
# node1 = TreeNode(2)
# node2 = TreeNode(3)
# root.children.append(node1)
# root.children.append(node2)
root  = takeInput()
printTree(root)

