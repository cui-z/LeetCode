"""
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。

示例
输入:
[
[1,3,1],
[1,5,1],
[4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
"""

def slove(nums):
    dp = [ [0 for _ in range(len(nums[0]))] for _ in range(len(nums))]
    dp[0][0] = nums[0][0]

    for i in range(1,len(nums)):
        dp[i][0] = dp[i-1][0] + nums[i][0]
    for j in range(1,len(nums)):
        dp[0][j] = dp[0][j-1]+nums[0][j]

    for i in range(1,len(nums)):
        for j in range(1,len(nums[0])):
            dp[i][j] = min(dp[i-1][j],dp[i][j-1])+nums[i][j]
    return dp[-1][-1]

print(slove([
[1,3,1],
[1,5,1],
[4,2,1]
]))