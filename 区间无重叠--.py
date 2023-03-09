"""
给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。

注意:
可以认为区间的终点总是大于它的起点。
区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。

示例
示例 1:
输入: [ [1,2], [2,3], [3,4], [1,3] ]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。

示例 2:
输入: [ [1,2], [1,2], [1,2] ]
输出: 2
解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。

示例 3:
输入: [ [1,2], [2,3] ]
输出: 0
解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
"""

"""
思路 
为了解决无重叠区间的问题，我们先将所有区间按照起点或者终点排序。

初始情况。这里，我们定义一个长度与输入数组intervals一致的dp数组，dp[i]表示intervals[0:i+1]这i个区间中，可以构成无重复区间的最长区间个数。

递推公式及其条件。我们需要从左到右遍历排序好了的所有区间，例如当前所考察的区间是intervals[i]，而intervals[0:i]这些区间还需要逆序遍历，找出来一个
  区间intervals[j]，如果可以满足intervals[i]和intervals[j]之间不存在重叠，那么可以考虑将dp[j]+1作为dp[i]的候选值，这里逆序的原因是为了减少寻找区间
  的次数，因为找到一个intervals[j]之后，在j左边的那些区间一定不会比intervals[j]更容易获取最长无重叠区间，就可以直接跳出当前i的循环了。

最后返回时，dp[-1]表示的是去除重叠区间后的最长无重叠区间的个数，所以需要同全部区间长度做差得到去除的区间个数。
"""

def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    dp = [1 for _ in range(len(intervals))]
    for i in range(len(intervals)):
        for j in range(i-1, -1, -1):
            if intervals[j][1] <= intervals[i][0]:
                dp[i] = max(dp[i], dp[j]+1)
                break
    return len(intervals) - dp[-1]


print(eraseOverlapIntervals([[1,2], [1,2], [1,2],[3,5],[4,5]]))
