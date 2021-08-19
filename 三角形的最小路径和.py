'''
给定一个三角形  找出自顶向下的最小路径和 每一步只能移动到下一行中相邻的结点

例如
[
   [2],
  [3,4],
 [6,5,7],
[4,1,8,3]
]

2 3 5 1  =11
'''

def slove(nums):
    dp = [[0 for _ in range(i)] for i in range(1,len(nums)+1)]

    print(dp)
    for i in range(len(nums)-1,-1,-1):
        for j in range(i+1):
            if i == len(nums)-1:
                dp[i][j] = nums[i][j]
            else:
                dp[i][j] = min(dp[i+1][j],dp[i+1][j+1])+nums[i][j]
    print(dp)
    return dp[0][0]

print(slove([
   [2],
  [3,4],
 [6,5,7],
[4,1,8,3]
]))
