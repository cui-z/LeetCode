'''
在一个由0和1组成的二维矩阵中，找到
只包含1的最大正方形，并返回其面积

找出最大边长就是最大的面积
'''

def slove(matrix):
    dp=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    length = 0
    for i in range(len(matrix)):
        if matrix[i][0] == 1:
            dp[i][0] = 1
            length=1
    for j in range(len(matrix[0])):
        if matrix[0][i] == 1:
            dp[0][j] = 1
            length=1


    for i in range(1,len(matrix)):
        for j in range(1,len(matrix[0])):
            if matrix[i][j] == 1:
                dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
                length = max(length,dp[i][j])

    return length*length

print(slove([
    [1,1,0,1],
    [1,1,1,1],
    [0,1,1,1],
    [1,1,1,1]
]))