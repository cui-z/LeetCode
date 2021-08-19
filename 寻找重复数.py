'''
1-n的数组，只有一个重复的整数，求这个整数
'''

def slove(nums):

    return (sum(nums)-sum(set(nums)))/(len(nums)-len(set(nums)))

print(slove([1,2,2,3]))