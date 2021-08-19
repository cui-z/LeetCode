'''
给定一个二维的矩阵，包含X和O
请找出所有被X包围的区域 并将区域里面的O用X填充
'''

def dfs(grid,i,j):
    if i<0 or i >= len(grid) or j <0 or j > len(grid) or grid[i][j]!="O":
        return
    grid[i][j]="#"
    dfs(grid,i-1,j)
    dfs(grid,i,j+1)
    dfs(grid,i+1,j)
    dfs(grid,i,j-1)

def  slove(grid):

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=="O" and(i==0 or i ==len(grid)-1 or j ==0 or j==len(grid[0])-1) :
                dfs(grid,i,j)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "#":
                grid[i][j] ="O"
            else:
                grid[i][j] ="X"

    return grid

print(slove([
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
]))

