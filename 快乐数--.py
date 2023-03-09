"""
描述

编写一个算法来判断一个数是不是“快乐数”。
一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，
       也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。

示例

输入: 19
输出: true
解释:
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6** + 8**2 = 100
1**2 + 0**2 + 02** = 1
"""


def slove(strs):

    tmp=set()
    tmp.add(int(strs))
    while True:
        resu= 0
        for s in strs:
            resu += int(s)*int(s)
        if resu in tmp :
            return False
        if resu ==1 :
            return True
        tmp.add(resu)
        strs = str(resu)

print(slove("61"))