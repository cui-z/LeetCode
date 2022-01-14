"""
解题思路：堆排序 总体思路：维护一个大小为 k 的最小堆，堆顶是这 k 个数里的最小的，遍历完数组后返回堆顶元素
51 即可。其时间复杂度为 O(nlogk)，因此堆排序这种解法在总体数据规模 n 较大，而维护规模 k 较小时对时 间复杂度的优化会比较明显。

"""

def slove(nums,k):
    import heapq
    resu =[]

    for n in nums:
        heapq.heappush(resu,n)
        if len(resu) >k:
            heapq.heappop(resu)
    return resu[0]


print(slove([1,2,3,4,56,6,7,3,5,6],3))