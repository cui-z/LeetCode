'''
给一个链表 返回链表开始入环的第一个节点 如果无环 返回null


记住
   链表头到环入口的距离 = 相遇点到环入口的距离+（k-1)圈长度
   所以两个指针分别从链表头和相遇点出发  一定相遇在相交点
'''


def slove(head):
    if not head or not head.next:
        return None
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if slow != fast:
        return None

    fast = head
    while fast != slow:
        slow = slow.next
        fast = fast.next
    return fast
