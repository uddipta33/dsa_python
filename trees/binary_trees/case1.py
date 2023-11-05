#Code: Construct Tree from Preorder and Inorder

from BinaryNodeClass import *
from BinaryUse import *

def apply(preorder, preStart, preEnd, inorder, inStart, inEnd):
    if(preStart > preEnd or inStart > inEnd):
        return None

    rootData = preorder[preStart]
    root = BinaryTreeNode(rootData)

    i=0
    while(i<=inEnd):
        if(inorder[i]==rootData):
            break
        i+=1
    
    rootIndex = i
    numsLeft = rootIndex - inStart
    root.left = apply(preorder, preStart+1, preStart+numsLeft, inorder, inStart, rootIndex-1)
    root.right = apply(preorder, preStart+numsLeft+1, preEnd, inorder, rootIndex+1, inEnd)
    return root


preorder = [1,2,4,5,3,6,8,9,7]
inorder = [4,2,5,1,8,6,9,3,7]
n = len(preorder)
root = apply(preorder, 0, n-1, inorder, 0, n-1)
printLevelWise(root)