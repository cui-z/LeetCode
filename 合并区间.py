"""
给出一个区间的集合，请合并所有重叠的区间。

示例 1
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。


先把所有区间按照开始位置排序，准备结果列表，逐个遍历，查看新加入结果列表的区间是否与结果列表最后一个区间重合，若重合则更新，否则直接加入结果列表。
"""

def  slove(nums):
    nums.sort(key = lambda a:a[0])
    result =[]
    for i  in range(len(nums)):
        if i==0 or (nums[i][0] > result[-1][1]):
            result.append(nums[i])
        else:
            result[-1][1] = max(result[-1][1],nums[i][1])

    return result

print(slove([[1,3],[8,10],[2,6],[15,18]]))