'''
给定一个数组 他的第i个元素是一支股票第i天的价格
你最多完成一笔交易 一次买 和 卖 计算最大利润
'''


def slove1(nums):

    dp=[0 for _ in range(len(nums))]
    min_num=nums[0]
    for i in range(1,len(nums)):
        if nums[i] > min_num:
            dp[i] = max(nums[i]-min_num,dp[i-1])
        else:
            min_num = nums[i]

    return dp[-1]

def slove(nums):

    result=0
    min_num=nums[0]
    for i in range(1,len(nums)):
        if nums[i] > min_num:
            result= max(nums[i]-min_num,result)
        else:
            min_num = nums[i]

    return result

print(slove1([7,1,5,3,6,4]))
print(slove([7,1,5,3,6,4]))