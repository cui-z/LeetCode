"""
给定一个二叉树，检查它是否是镜像对称的。
"""

class Solution:
    def isSymmetric(self, root):
        if not root:
            return True

        que = [root]
        while que:
            this_level_length = len(que)

            # //2 的目的是为了 成对的取出 进行比较
            for i in range(this_level_length // 2):
                # 要么其中一个是None但另外一个不是
                if (not que[i] and que[this_level_length - 1 - i]) or (que[i] and not que[this_level_length - 1 - i]):
                    return False
                # 要么两个都不是None
                if que[i] and que[i].val != que[this_level_length - 1 - i].val:
                    return False
            for i in range(this_level_length):
                if not que[i]: continue
                que.append(que[i].left)
                que.append(que[i].right)
            # 每次取出新加的部分
            que = que[this_level_length:]
        return True