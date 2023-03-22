"""
给你一个链表数组，每个链表都已经按升序排列。请你将所有链表合并到一个升序链表中，返回合并后的链表。

   示例 1：

      输入：lists = [[1,4,5],[1,3,4],[2,6]]
      输出：[1,1,2,3,4,4,5,6]


思路：
    模仿合并多个有序数组的方式 需要注意的是  链表没有pop(0)的操作 只能是第一步先把val 和索引添加上  通过堆取出最小值  添加到结果链表上 然后利用链表的next获取链表的下一个元素



当然由于k个链表是有序的，我们实际上只需要维护k个指针从k个链表的头向尾滑动，每次选取k个链表的表头里的最小加入新的有序链表里。

这里我们就可以借用最小堆(优先队列)维护k个链表的当前头位置的值。
时间复杂度就变成O(N*logK)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        head = point = ListNode(0)

        res =[]
        for k,v in enumerate(lists):
            if v != None:
                res.append((v.val,k))
        heapq.heapify(res)

        while res:
            cur = heapq.heappop(res)
            point.next = ListNode(cur[0])
            point = point.next
            lists[cur[1]] = lists[cur[1]].next
            if lists[cur[1]]:
                heapq.heappush(res,(lists[cur[1]].val,cur[1]))
        return head.next