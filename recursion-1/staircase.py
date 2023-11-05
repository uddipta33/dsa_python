#A child is running up a staircase with N steps, 
# and can hop either 1 step, 2 steps or 3 steps at a time. 
# Implement a method to count how many possible ways the child can run up to the stairs. 
# You need to return number of possible ways W.
def stair(n):
    if(n==0):
        return 1
    if(n<0):
        return 0
    
    x = stair(n-1)
    y = stair(n-2)
    z = stair(n-3)

    return x+y+z

print(stair(5))