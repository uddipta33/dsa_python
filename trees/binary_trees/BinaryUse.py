from BinaryNodeClass import *
from queue import Queue

def printTree(root):
    if(root is None):
        return
    print(root.data, end = " : ")
    if(root.left != None):
        print(root.left.data, end = " ")
    if (root.right != None):
        print(root.right.data)
    print("")
    printTree(root.left)
    printTree(root.right)

def takeInput():
    rootData = int(input("Enter data : "))
    if rootData == -1:
        return None
    root = BinaryTreeNode(rootData)
    leftChild = takeInput()
    rightChild = takeInput()
    root.left = leftChild
    root.right = rightChild
    return root

def takeInputLevelWise():
    rootData = int(input("Enter root data : "))
    if(rootData == -1):
        return None
    root = BinaryTreeNode(rootData)
    pendingNodes = Queue()
    pendingNodes.put(root)
    while(pendingNodes.qsize() != 0):
        front = pendingNodes.get()
        leftData = int(input("Enter left child of {} ".format(front.data)))
        if(leftData!=-1):
            leftChild = BinaryTreeNode(leftData)
            front.left = leftChild
            pendingNodes.put(leftChild)
        rightData = int(input("Enter right child of {} ".format(front.data)))
        if(rightData!=-1):
            rightChild = BinaryTreeNode(rightData)
            front.right = rightChild
            pendingNodes.put(rightChild)
    
    return root
        
    
def printLevelWise(root):
    if (root is None):
        return 
    pendingNodes = Queue()
    pendingNodes.put(root)
    while(pendingNodes.qsize()!=0):
        front = pendingNodes.get()
        print(front.data, end=" : ")
        if(front.left):
            print("L:", front.left.data, end=" ")
            pendingNodes.put(front.left)
        else:
            print("L:-1", end=" ")
        if(front.right):
            print("R:", front.right.data)
            pendingNodes.put(front.right)
        else:
            print("R:-1")
    
def numNodes(root):
    if(root is None):
        return 0
    return 1 + numNodes(root.left) + numNodes(root.right)

def findNode(root, x):
    if(root is None):
        return False
    
    if (root.data == x):
        return True
    ans1 = findNode(root.left, x)
    ans2 = findNode(root.right, x)
    return (ans1 or ans2)

def inorder(root):
    if(root is None):
        return
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)

def preorder(root):
    if(root is None):
        return
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)

# root = BinaryTreeNode(1)
# n1 = BinaryTreeNode(2)
# n2 = BinaryTreeNode(3)
# root.left = n1
# root.right = n2

# 1 2 3 4 5 6 7 -1 -1 -1 -1 8 9 -1 -1 -1 -1 -1 -1
# root = takeInputLevelWise()
# # printLevelWise(root)
# print(findNode(root, 7))
# inorder(root)
# preorder(root)