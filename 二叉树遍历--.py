'''
递归版本  最为简单
'''
#前序
def slove(root):
    if not root:
        return
    print(root.val)
    slove(root.left)
    slove(root.right)

#中序
def slove1(root):
    if not root:
        return
    slove1(root.left)
    print(root.val)
    slove1(root.right)

#后序
def slove2(root):
    if not root:
        return
    slove2(root.left)
    slove2(root.right)
    print(root.val)


'''
非递归版本
'''
'''
前序遍历
申请一个list 初始默认root

while list:
将list最后一个元素pop出来  添加到最终结果
添加pop出来元素的右节点
添加pop出来元素的左节点
'''
def slove4(root):
    stack = [root]
    result=[]
    while stack:
        curr = stack.pop()
        result.append(curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
    return result

'''
中序遍历

'''
def slove5(root):
    if not root:
        return []
    stack = []  # 不能提前将root结点加入stack中
    result = []
    cur = root
    while cur or stack:
        # 先迭代访问最底层的左子树结点
        if cur:
            stack.append(cur)
            cur = cur.left
        # 到达最左结点后处理栈顶结点
        else:
            cur = stack.pop()
            result.append(cur.val)
            # 取栈顶元素右结点
            cur = cur.right
    return result


'''
后序

只需要修改 前序的代码即可
'''


def slove6( root):
    """
    左->右->根
    :type root: TreeNode
    :rtype: List[int]

    中左右  调整  中右左  反转结果   左右中
    """
    stack1 = [root]
    stack2 = []
    while stack1:
        cur = stack1.pop()
        stack2.append(cur.val)
        if cur.left:
            stack1.append(cur.left)
        if cur.right:
            stack1.append(cur.right)
    return stack2[::-1]


'''
层次遍历
'''

def slove(root):
    stack=[root]
    result=[]

    while stack:
        tmp=[]
        for i in range(len(stack)):
            cur = stack.pop(0)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
            tmp.append(cur.val)
        result.append(tmp)
    return  result
