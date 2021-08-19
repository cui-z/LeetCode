
'''
删除链表中等于给定值val的所有节点

例如  1 2 6 3 4 6    val =6
1 2 3 4
'''
class ListNode():
    pass

def slove(head,val):
    #新建一个链表  用来表示前一个
    dump = ListNode(0)
    dump.next = head
    pre =dump
    last = head
    while last:
        if last.val ==val:
            pre.next = last.next
            last = last.next
        else:
            pre = pre.next
            last = last.next
    return dump.next