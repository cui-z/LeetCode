'''
给定一个范围在1-n的整形数字，n为数组大小，数组中的元素一些出现了
两次，有些只有一次
找出1-n范围内没有出现的数字
'''

#1-n之间  长度为n 不使用额外空间 且n

def slove(nums):
    for n in nums:
        n = abs(n)
        nums[n-1] = -abs(nums[n-1])
    return [ k+1 for k,v in enumerate(nums)if v >0]


print(slove([4,3,2,7,8,2,3,1]))