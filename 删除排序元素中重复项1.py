'''
给定一个排序数组 原地删除重复的元素 使得每个元素只出现一次
返回移除后数组的新长度
'''


def slove(nums):
    length = len(nums)
    curr=1
    while curr < length:
        if nums[curr] == nums[curr-1]:
            nums.remove(nums[curr])
            length-=1
        else:
            curr+=1
    return length

print(slove([1,1,2]))