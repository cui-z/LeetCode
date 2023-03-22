"""
给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。

示例

给定这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5

解题思路
1.遍历整个链表，记录有多少个节点
2.计算需要翻转几段
3.每段都翻转一下
4.每段之间尾头相连

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        cur = head
        count = 0
        # 统计有多少节点
        while head:
            count += 1
            head = head.next
        # 计算要翻转几组
        n = count // k
        # 不用翻转直接返回原链表
        if n == 0:
            return cur

        tail = dummy
        for i in range(n):
            t = cur
            count = 0
            cur, pre = cur.next, cur
            # 翻转链表
            while count < k - 1:
                count += 1
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
                # cur.next, cur, pre = pre, cur.next, cur
            # 尾头相接
            tail.next = pre
            tail = t
        # 把最后一段接上
        t.next = cur

        return dummy.next