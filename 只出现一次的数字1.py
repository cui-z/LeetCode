'''

给一个数组 除了某个元素出现一次 其余元素都是出现两次
找出出现一次的元素
'''

def slove(nums):
    return sum(set(nums))*2 - sum(nums)

print(slove([2,3,3,6,6,4,4]))