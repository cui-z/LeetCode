'''
给定两个字符串s1和s2 计算出s1转换为s2所需要的最少操作次数
可以的三种操作
插入一个字符
删除一个字符
替换一个字符

解析：https://zhuanlan.zhihu.com/p/105538493
dp[i][j] 代表着word1的前i个字符转换成word2的前j个字符所需要的最少操作步数
'''


def slove(x,y):
    dp = [[0 for _ in range(len(y)+1)] for _ in range(len(x)+1)]

    for i in range(1,len(y)+1):
        dp[0][i] = dp[0][i-1]+1
    for i in range(1,len(x)+1):
        dp[i][0] = dp[i-1][0]+1
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                dp[i+1][j+1] = dp[i][j]
            else:
                dp[i+1][j+1] = min(dp[i+1][j],dp[i][j+1],dp[i][j])+1
    return dp[-1][-1]

print(slove("horse","ros"))