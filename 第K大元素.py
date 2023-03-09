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
    #return heapq.heappop(resu)
    return resu[0]


#快速排序的思路
def slove1(nums,first,last,k):
    # if first >= last:
    #     return
    mid = nums[first]
    l = first
    r =last
    while l < r:
        while l < r and nums[r] < mid:
            r -= 1
        nums[l] = nums[r]
        while l < r and nums[l] > mid:
            l += 1
        nums[r] = nums[l]
    nums[l] = mid
    if l+1 > k:
        return slove1(nums,first,l-1,k)
    elif l+1< k:
        return slove1(nums,l+1,last,k)
    else:
        return nums[l]

l=[2,3,1,5,4,6]
print(slove(l,3))
print(slove1(l,0,len(l)-1,3))