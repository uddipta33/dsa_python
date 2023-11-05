from BinaryNodeClass import *
from BinaryUse import *

def getDiameter(root):
    if(root is None):
        return 0,0
    lh,ld = getDiameter(root.left)
    rh, rd = getDiameter(root.right)
    
    height = 1 + max(lh,rh)
    diameter = max(lh+rh, max(ld,rd))
    return height,diameter 

root = takeInputLevelWise()
h,d = getDiameter(root)
print("height : ",h)
print("diameter : ",d)