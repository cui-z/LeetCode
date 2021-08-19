# 给定一个链表 删除链表倒数第n个节点并返回头结点

def slove(head,n):
    fast = head
    for _ in range(n):
        fast=fast.next

    if not fast:
        return head.next

    slow =head
    while fast.next:
        fast =fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head