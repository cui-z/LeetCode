"""
给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口 k 内
的数字。滑动窗口每次只向右移动一位。

返回滑动窗口最大值。

示例

输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
输出: [3,3,5,5,6,7]
解释:
滑动窗口的位置 最大值
[1 3 -1] -3 5 3 6 7 3
1 [3 -1 -3] 5 3 6 7 3
1 3 [-1 -3 5] 3 6 7 5
1 3 -1 [-3 5 3] 6 7 5
1 3 -1 -3 [5 3 6] 7 6
1 3 -1 -3 5 [3 6 7] 7


看代码理解

"""


def solve( nums, k):
    n = len(nums)
    if n < 2 or k == 1:
        return nums
    res = []
    index = [0]
    for i in range(1, n):

        if index[0] <= i - k:
            index.pop(0)
        while index and nums[index[-1]] < nums[i]:
            index.pop()
        index.append(i)
        if i >= k - 1:
            res.append(nums[index[0]])
    return res

print(solve([1,3,-1,-3,5,3,6,7],3))