'''
给定一个非负整数组成的非空数组  在该数的基础上加1 返回一个新的数组
除了整数0 以外  整数不会以0开头
【4 3 2 1】 【4 3 2 2】
'''

def slove(nums):
    for i in range(len(nums)-1,-1,-1):
        if nums[i] < 9:
            nums[i]+=1
            return nums
        else:
            nums[i] = 0
    return [1]+nums

print(slove([9,9]))