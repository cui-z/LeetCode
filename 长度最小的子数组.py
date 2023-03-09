"""
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。

示例

输入: s = 7, nums = [2,3,1,2,4,3]
输出: 2
解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。
"""

# 跟某一个题目很类似  和为k的子数组


def minSubArrayLen( s, nums):
    """
    :type s: int
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    start = 0
    min_len = n + 1
    cur_sum = 0
    for i in range(n):
        cur_sum += nums[i]
        while cur_sum >= s:
            min_len = min(min_len, i - start + 1)
            cur_sum -= nums[start]
            start += 1
    return min_len if min_len <= n else 0