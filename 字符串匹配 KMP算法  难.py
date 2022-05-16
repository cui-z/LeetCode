"""
KMP算法是经典字符串匹配算法，时间复杂度为O(m+n)，n为主串长度，m为模式串长度。

参考
https://www.zhihu.com/question/21923021/answer/281346746

"""
def strStr(haystack, needle):
    def KMP(s, p):
        """s为主串  p为模式串   如果t里有p，返回打头下标
        """
        nex = getNext(p)
        print(nex)
        i = 0
        j = 0   # 分别是s和p的指针
        while i < len(s) and j < len(p):
            if j == -1 or s[i] == p[j]: # j==-1是由于j=next[j]产生
                i += 1
                j += 1
            else:
                j = nex[j]
        if j == len(p): # j走到了末尾，说明匹配到了
            return i - j
        else:
            return -1
    def getNext(p):
        """p为模式串   返回next数组，即部分匹配表
        """
        nex = [0] * (len(p) + 1)
        nex[0] = -1
        i = 0
        j = -1
        while i < len(p):
            if j == -1 or p[i] == p[j]:
                i += 1
                j += 1
                nex[i] = j     # 这是最大的不同：记录next[i]
            else:
                j = nex[j]
        return nex
    return KMP(haystack, needle)