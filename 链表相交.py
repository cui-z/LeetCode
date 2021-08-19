
def slove(headA,headB):
    comp={}
    while headA:
        comp[headA] =1
        headA = headA.next

    while headB:
        if headB in comp:
            return headB
        headB = headB.next
    return None