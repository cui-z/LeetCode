'''
给定一个字符串 计算字符串中有多少个回文子串
具有不同开始位置和结束位置的子串  即使字符相同 也会被认为不同的子串
'''

def slove(s):
    result = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if s[i:j] ==s[i:j][::-1]:
                result+=1
    return  result


def countSubstrings( s):
    """
    MyMethod1
    算法：动规
    思路：
        联想第5题，用动规记录和求出字符串s的所有是回文串的子字符串，然后用计数器counter技术
        一样也是先从单个字符是回文的dp[i][i]= True开始记录
        再到两个字符dp[i][i+1]  = s[i]==s[i+1]
        再到后面的多个字符的回文dp[i][j] = (dp[i+1][j-1] and s[i+1]==s[j-1])
        还是要注意遍历的方式
        for j in range(1，n)
            for i in range(j-1)
        先从j开始遍历，代表以j结束的子串，然后i再从0开始去循环到j
    """
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    counter = 0
    for i in range(n):
        dp[i][i] = True
        counter += 1
    for i in range(1, n):
        if s[i - 1] == s[i]:
            dp[i - 1][i] = True
            counter += 1
    for j in range(1, n):
        for i in range(j - 1):
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                counter += 1
    return counter


# 简化版
def slove(s):
    res = len(s)
    dp = [[True if j == i else False for j in range(len(s))] for i in range(len(s))]

    for i in range(1, len(s)):
        for j in range(i):
            if i - j == 1:
                if s[i] == s[j]:
                    dp[i][j] = True
                    res += 1
            else:
                if (s[i] == s[j]) and dp[i - 1][j + 1]:
                    dp[i][j] = True
                    res += 1

    return res

print(slove("aaa"))
print(countSubstrings("aaa"))