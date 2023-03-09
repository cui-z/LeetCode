"""
给定一个无序列表，列表中元素均为不重复的整数。请找出列表中有没有比它前面元素都大，比它后面的元素都小的数，如果不存在则返回-1，存在则显示其索引。
其中左边无限小 右边无限大

[1,2,3,1,4,5,7,6] 输出 [4,5]


一个数要比它左边的所有数要大，比右边的所有数要小，那么它必定大于左边元素的最大值，同时小于右边元素的最小值。
两次遍历。第一次遍历从后向前，找出第 i 个元素右边元素的最小值，保存在 rightMin 数组中。第二次遍历，从前向后，使用一个临时变量保存左边元素的最大值，一边判断一边更新。
"""

def slove(nums):
    r_min=nums[-1]
    r_nums = [float("inf")]
    result=[]

    for i in range(len(nums)-1,-1,-1):
        if nums[i] < r_min:
            r_min = nums[i]
        r_nums.append(r_min)

    l_max = -float('inf')
    for i in range(len(nums)):
        if nums[i] > l_max:
            l_max=nums[i]
            if nums[i] < r_nums[::-1][i+1]:
                result.append(nums[i])
    return result


print(slove([1,2,3,1,4,5,7,6]))
print(slove([1,2,3,1,4,0,4,5]))
print(slove([1,2,3,4,5,6]))