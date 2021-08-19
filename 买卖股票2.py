'''
给定一个数组 他的第i个元素是一支股票第i天的价格
你可以多次进行交易 求最大利润
'''

def slove(nums):
    sum=0
    for i in range(1,len(nums)):
        if nums[i] >nums[i-1]:
            sum+=(nums[i]-nums[i-1])
        else:
            pass
    return sum

print(slove([7,1,5,3,6,4]))