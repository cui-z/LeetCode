"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。


跟 盛水最多的容器  不一样

https://github.com/labuladong/fucking-algorithm/blob/master/%E9%AB%98%E9%A2%91%E9%9D%A2%E8%AF%95%E7%B3%BB%E5%88%97/%E6%8E%A5%E9%9B%A8%E6%B0%B4.md
"""

def  slove(nums):
    l = 0
    r = len(nums) -1
    result =0
    max_l = nums[0]
    max_r = nums[-1]
    while l <= r:
        max_l = max(max_l,nums[l])
        max_r = max(max_r,nums[r])
        if max_l < max_r:
            result += max_l-nums[l]
            l+=1
        else:
            result += max_r -nums[r]
            r-=1
    return result

print(slove([0,1,0,2,1,0,1,3,2,1,2,1]))