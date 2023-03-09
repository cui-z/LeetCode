"""
有一只地鼠不小心跑进了一个m*n的矩形田地里，假设地鼠在这块田地的初始位置为（x,y），'
    并且每次只能向相邻的上下左右四个方向移动一步，那么在最多移动K次的情况下，有多少
    条路径可以逃出这片田地（一旦出去田地的边界就不能再往回走）？
"""

res = 0


def move(m, n, x, y, k):
    def slove(m, n, x, y, k):
        global res
        if (x == -1 or x == m or y == -1 or y == n):
            res += 1
            return
        if k == 0:
            return
        slove(m, n, x - 1, y, k - 1)
        slove(m, n, x + 1, y, k - 1)
        slove(m, n, x, y - 1, k - 1)
        slove(m, n, x, y + 1, k - 1)

    slove(m, n, x, y, k)
    return res

print(move(5,4,3,2,2))