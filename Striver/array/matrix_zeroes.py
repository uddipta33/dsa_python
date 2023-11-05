#Given a matrix if an element in the matrix is 0 then you will have to set its entire column and row to 0 and then return the matrix.

#Better solution 0(n^2) space = O(m)+O(n)
def matZeroes(arr):
    nrows = len(arr)
    mcols = len(arr[0])
    row = [0]*nrows
    col = [0]*mcols
    for i in range(nrows):
        for j in range(mcols):
            if arr[i][j]==0:
                row[i]=1
                col[j]=1
    
    for i in range(nrows):
        for j in range(mcols):
            if(row[i]==1 or col[j]==1):
                arr[i][j]=0

#optimal solution space = O(1)
def optimalMatrix(arr):
    nrows = len(arr)
    mcols = len(arr[0])
    col0=1
    #row = arr[...][0]
    #col = arr[0][...]
    for i in range(nrows):
        for j in range(mcols):
            if(arr[i][j]==0):
                arr[i][0]=0
                if(j!=0):
                    arr[0][j]=0
                else:
                    col0=0
    
    for i in range(1,nrows):
        for j in range(1,mcols):
            if(arr[i][0] == 0 or arr[0][j]==0):
                arr[i][j]=0
    if(arr[0][0]==0):
        for j in range(mcols):
            arr[0][j]=0
    if(col0==0):
        for i in range(nrows):
            arr[i][0]=0


arr = [[1,1,1],[1,0,1],[1,1,1]]
# matZeroes(arr)
optimalMatrix(arr)
print(arr)

                
