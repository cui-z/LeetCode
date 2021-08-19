'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）机器人每次只能向
下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）现在考虑网格
中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 1 和 0 来表示。
'''
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) :
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for i in range(m)]  # 初始化dp数组元素全0
        # 针对第一列的某个位置判断是否有障碍物，决定该处dp取值
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            else:
                dp[i][0] = 1
        # 针对第一行的的某个位置判断是否有障碍物，决定该处dp取值
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            else:
                dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:  # 有障碍物时，dp[i][j]=0
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]  # 没有障碍物时
        return dp[-1][-1]