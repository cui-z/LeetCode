'''

给定一个链表  对每两个相邻的节点作交换 并返回头结点

1 2 3 4   2 1 4 3
'''
class ListNode():
    pass

def slove(head):
    dummy = ListNode(0)
    dummy.next = head
    pre = dummy
    cur = head
    while cur and cur.next:
        pre.next = cur.next
        cur.next = cur.next.next
        pre.next.next = cur
        pre=cur
        cur= cur.next
    return dummy.next
