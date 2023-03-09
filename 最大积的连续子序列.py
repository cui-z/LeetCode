'''

给定一个数组nums,找出一个序列中 乘积最大的连续子序列
该序列至少包含一个数‘

有正负
'''


def slove(nums):
    dp_min = [0 for i in range(len(nums))]
    dp_max = [0 for i in range(len(nums))]
    dp_max[0] = nums[0]
    dp_min[0] = nums[0]
    max_result = nums[0]
    for i in range(1, len(nums)):
        dp_min[i] = min(nums[i], dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i])
        dp_max[i] = max(nums[i], dp_min[i - 1] * nums[i], dp_max[i - 1] * nums[i])
        max_result = max(dp_max[i], dp_min[i],max_result)
    return max_result


print(slove([2, 3, -2, 4]))
