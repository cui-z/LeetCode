
'''
给定一个单链表  把所有的偶数节点和奇数节点分别排在一起 奇数节点和偶数节点是指节点编号
  的奇偶性

1 2 3 4 5 null   结果为 1 3 5 2 4 null

'''

class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def slove(head):
    if head is None:
        return head

    even_head ,odd ,even = head.next,head,head.next

    while even is not None and even.next :
        odd.next = even.next
        even.next = even.next.next
        odd = odd.next
        even = even.next
    odd.next = even_head
    return head