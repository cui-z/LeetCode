"""
题目描述：
输入一个递增排序的数组和一个数字S，在数组中查找两个数，是的他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
"""

"""
第一，小的数字在前面，这个没问题。第二，题目中要求当存在多个组合的时候，返回其中的乘积最小的一个。我们从两头向中间的移动过程中找到的第一组一定是乘积最小的。原因如下：

我们把两个数字想成矩形的两条边，根据中学的知识，当两条边越接近，面积越大（乘积越大）。由于从两头向中间进行查找的，找到的第一个组合一定是边差距最大的，所以乘积最小。
"""


def FindNumbersWithSum( array, tsum):
    if not array: return []
    left, right = 0, len(array) - 1
    while left < right:
        _sum = array[left] + array[right]
        if _sum > tsum:
            right -= 1
        elif _sum < tsum:
            left += 1
        else:
            return [array[left], array[right]]
    return []

print(FindNumbersWithSum([1,2,3,4,5,6,8,9],7))
