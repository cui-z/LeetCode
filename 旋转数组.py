
'''
给定一个数组 将数组中元素向右移动k个位置，其中k是非负数

例 【1,2,3,4，5,6,7】 k=3
[5,6,7,1,2,3,4]
'''


def slove(nums,k):
    while k >0:
        num = nums.pop()
        nums.insert(0,num)
        k-=1

    return nums

print(slove([1,2,3,4,5,6],3))