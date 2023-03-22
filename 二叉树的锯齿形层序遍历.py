"""
给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

输入：root = [3,9,20,null,null,15,7]
输出：[[3],[20,9],[15,7]]

层次遍历 加上标识符 实现正序 和逆序
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        result = []
        order = True

        while stack:
            tmp = []
            for i in range(len(stack)):
                cur = stack.pop(0)
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
                tmp.append(cur.val)

            result.append(tmp if order else tmp[::-1])
            order = not order
        return result
