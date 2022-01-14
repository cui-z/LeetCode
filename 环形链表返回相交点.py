'''
给一个链表 返回链表开始入环的第一个节点 如果无环 返回null

先行条件是快慢指针在P点相遇，且快指针速度是慢指针的2倍，则相遇时，快指针走过的路径长度是慢指针的2倍

       解：  设快慢指针在P点相遇时，慢指针在圆圈中走了m圈， 快指针走了n圈。

                则有：   2[c + m(a + b) + a] = c + n(a + b) + a            (1)

                 <=>     c = (n - 2m - 1) (a+b) + b              (2)

           由公式（2）我们可以知道，c刚好等于整数倍周长 + b ，如果一个指针在P点出发，一个在O点出发，当从O出发的指针到达Q点时，
           从P出发的指针刚好走了一个b + 整数倍的周长，然后出现在Q点，从而可知两个指针在Q点相遇。
—

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
