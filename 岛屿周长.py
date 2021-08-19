'''
给定一个包含0,1的二维网格地图，其中1代表陆地，0代表水域
整个网格被水完全包围，其中恰好一个岛屿
岛屿内部没有湖 求岛屿周长

'''

def slove(grid):
    direction = [[1,0],[0,1],[-1,0],[0,-1]]
    result=0
    w = len(grid)
    l = len(grid[0])
    for k in range(w):
        for v in range(l):
            if grid[k][v] == 1:
                tmp = 4
                for d1,d2 in direction:
                    if (0<=(k+d1) <w) and (0<=(v+d2)<l) and grid[k+d1][v+d2]==1:
                        tmp-=1
                result+=tmp
    return result

print(slove([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
