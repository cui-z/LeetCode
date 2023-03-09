'''
给定一个二叉树 找出其最大深度
'''

# 层次遍历的 演化版本
def slove(root):
    stack=[root]
    result=[]

    res=0
    while stack:
        res+=1
        tmp=[]
        for i in range(len(stack)):
            cur = stack.pop(0)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
            tmp.append(cur.val)
        result.append(tmp)
    return  res


"""

给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

说明: 叶子节点是指没有子节点的节点。
"""
def slove(root):
    stack=[root]
    result=[]

    res=0
    while stack:
        res+=1
        tmp=[]
        for i in range(len(stack)):
            cur = stack.pop(0)
            if not cur.left and not cur.right:
                return res
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
            tmp.append(cur.val)
        result.append(tmp)
    return  res