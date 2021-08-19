'''

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，这个地方的房屋围成一圈
，意味着第一家和最后一家是紧挨着的
同时相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报
警。
给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最
高金额。

【2 3 2】
结果 3
'''

#问题难点在于第一家和最后一家是连起来的 所以偷第一家就不能最后一家 最后一家就不能第一家

def  slove(nums):
    dp1 =[0 for _ in range(len(nums))]
    dp2 = [0 for _ in range(len(nums))]

    for i in range(len(nums)-1):
        dp1[i+1] = max(dp1[i],dp1[i-1]+nums[i])
    for j in range(1,len(nums)):
        dp2[j] = max(dp2[j-1],dp2[j-2]+nums[j])

    return max(dp2[-1],dp1[-1])

print(slove([1,2,3,1]))