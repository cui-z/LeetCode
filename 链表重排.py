"""
给定一个单链表 L 的头节点 head ，单链表 L 表示为：

L0 → L1 → … → Ln - 1 → Ln
请将其重新排列后变为：

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


有三步
找中点
翻转中点之后的链表
依次拼接
"""
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next: return head
        # 1 2 3 4 5
        fast = head
        pre_mid = head
        # 找到中点, 偶数个找到时上界那个
        while fast.next and fast.next.next:
            pre_mid = pre_mid.next
            fast = fast.next.next
        # 翻转中点之后的链表,采用是pre, cur双指针方法
        pre = None
        cur = pre_mid.next
        # 1 2 5 4 3
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        # 翻转链表和前面链表拼接
        pre_mid.next = pre
        # 1 5 2 4 3
        # 链表头
        p1 = head
        # 翻转头
        p2 = pre_mid.next
        #print(p1.val, p2.val)
        while p1 != pre_mid:
            # 建议大家这部分画图, 很容易理解
            pre_mid.next = p2.next
            p2.next = p1.next
            p1.next = p2
            p1 = p2.next
            p2 = pre_mid.next