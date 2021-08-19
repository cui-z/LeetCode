'''
给定一个链表  将链表向右旋转k个位置 k是非负数

例 1 2 3 4 5 null   k=2
结果  4 5 1 2 3 null
'''

def slove(head,k):
    #初始记为1
    long = 1
    curr = head
    while curr.next:
        curr = curr.next
        long+=1
    k%=long
    if k ==0:
        return  head
    slow = fast = head

    while fast.next:
        slow = slow.next
        fast = fast.next
    new_head = slow.next
    slow.next = None
    fast.next = head
    return  new_head