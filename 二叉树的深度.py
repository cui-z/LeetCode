'''
给定一个二叉树 找出其最大深度
'''

def slove(root):
    if root ==None:
        return
    else:
        return 1 + max(slove(root.left),slove(root.right))