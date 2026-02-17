#14-02-2026
#40marks
def maze(grid, i, j, n, path):
    if i>=n or j>=n or grid[i][j]==1:
        return
    if i==n-1 and j==n-1:
        print(path)
        return
    maze(grid, i, j+1, n, path+"R")
    maze(grid, i+1, j, n, path+"D")
grid= [[0,0,0],
       [0,1,0],
       [0,0,0]]
maze(grid,0,0,3," ")