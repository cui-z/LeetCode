"""
给出一个由无重复的正整数组成的集合，找出其中最大的整除子集，子集中任意一对 (Si，Sj) 都要满足：Si % Sj = 0 或 Sj % Si = 0。
如果有多个目标子集，返回其中任何一个均可。

示例
示例 1:
输入: [1,2,3]
输出: [1,2] (当然, [1,3] 也正确)

示例 2:
输入: [1,2,4,8]
输出: [1,2,4,8]
"""
def slove( nums):
    if len(nums) <= 1:
        return nums
    nums = sorted(nums)
    dp = {i: [nums[i]] for i in range(len(nums))}               # 至少子集可以做一个子集
    for i in range(1, len(nums)):                               # 求取每一个数字所对应的最大整数子集
        for j in range(i - 1, -1, -1):                          # 研究当前数字能够被小于这个数字的所有数整除
            if nums[i] % nums[j] == 0:                          # 如果遇到j可以被i整除，那么把j所对应的最大子集包含在i的位置。
                list_up_to_i = dp[j] + [nums[i]]                # 到j为止的最大子集
                dp[i] = max(list_up_to_i, dp[i], key=len)       # 由于可能有多个数可以被i整数，在子集中选最长的保存，每次都要更新
    return max(dp.values(), key=len)                            # 选出来所有值所对应的最长子集中最长的