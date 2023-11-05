from BinaryNodeClass import *
from BinaryUse import *

def sumNodes(root):
    if(root is None):
        return 0
    
    return root.data + sumNodes(root.left) + sumNodes(root.right)

root = takeInputLevelWise()
print(sumNodes(root))