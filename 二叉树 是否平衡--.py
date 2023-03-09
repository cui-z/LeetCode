"""
平衡二叉树定义：二叉树每个节点的左右子树高度差不超过 1；

思路：平衡二叉树满足根节点及其子节点都是平衡二叉树，所以需要递归计算每个节点左右子树的高 度，然
    后判断高度差是否不超过 1；参考代码如下：
"""

class Solution:
    def isBalanced(self, root) :
        if not root :
            return True
        result = abs(self.getHeight(root.right) - self.getHeight(root.left)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        return result
    def getHeight(self, root):
        if not root:
            return 0
        return max(self.getHeight(root.left), self.getHeight(root.right)) + 1