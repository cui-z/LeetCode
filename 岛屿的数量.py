'''
给定一个由 1（陆地）和0（水）组成的二维网格，可以假设被水包围，
求计算岛屿的数量
'''


#卡在了怎么感染的地方
def dfs(grid,i,j):
    if i <0 or j <0 or i >=len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
        return
    grid[i][j] = 0
    dfs(grid,i-1,j)
    dfs(grid,i+1,j)
    dfs(grid,i,j-1)
    dfs(grid,i,j+1)


def slove(grid):
    sum = 0
    direction = [[-1,0],[1,0],[0,1],[0,-1]]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(grid,i,j)
                sum+=1
    return sum


print(slove([
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,1,1]
]))