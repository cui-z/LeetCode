# 请检查一个链表是否为回文链表
class ListNode():
    pass


def slove(head):
    if not head or not head.next:
        return True

    fast = slow = prev = head

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = None

    curr = slow
    if not curr.next:
        right = slow
    else:
        while curr.next:
            tmp = ListNode(curr.next.val)
            tmp.next = slow
            slow = tmp
            curr.next = curr.next.next
        right = tmp

    left = head

    while left:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
