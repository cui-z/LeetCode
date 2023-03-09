'''

给定一个非负的整数数组 你最初位于数组的第一个位置

数组中的每一个元素代表你可以跳跃的最大长度
判断你是否能到达最后一个位置

'''


def slove(nums):
    r=len(nums)-1
    l= r-1
    while l >=0:
        if nums[l]+l >= r:
            r=l 
        l-=1
    return r==0

print(slove([3,2,1,0,4]))
