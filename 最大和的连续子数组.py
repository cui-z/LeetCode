'''
给定一个整数数组 找到一个具有最大和的连续的子数组
返回其最大和
'''

def slove(nums):

    dp=[0 for _ in range(len(nums))]
    dp[0]=nums[0]

    for i in range(1,len(nums)):
        dp[i] = max(dp[i-1]+nums[i],nums[i])

    return max(dp)

print(slove([-2,1,-3,4,-1,2,1,-5,4]))