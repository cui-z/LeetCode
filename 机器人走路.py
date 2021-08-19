'''
机器人位于 M x N网格的左上角 每次只能向右向下走  走到右下角有多少不同路径
'''

def slove(m,n):
    dp = [[1 for _ in range(n)] for _ in range(m)]
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j] = dp[i-1][j] +dp[i][j-1]
    return dp[-1][-1]