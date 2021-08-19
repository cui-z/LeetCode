'''
合并两个已经排序的列表 并将其作为一个新的列表返回
  新列表应该通过拼接前两个列表的节点来完成

'''

class ListNode():
    pass

def  slove(l1,l2):
    if not l1 and not l2:
        return None
    elif not l1:
        return l2
    elif not l2:
        return l1
    new_head = ListNode(0)
    curr = new_head
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1= l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    if l1:
        curr.next = l1
    elif l2:
        curr.next = l2
    return  new_head.next