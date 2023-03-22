"""
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]


思路 参考链表反转和 k个一组反转链表
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0)
        dummy.next =head
        cur =head
        d = dummy
        #重新赋值 是因为在下面对left进行了修改
        l = left

        while left-1 >0:
            cur =cur.next
            d = d.next
            left -= 1
        num= right-l
        pre =cur
        cur = cur.next
        t=pre
        while num > 0:
            print(num)
            print("------")
            next = cur.next
            num -=1
            cur.next = pre
            pre= cur
            cur =next
        t.next = cur
        d.next = pre

        return dummy.next