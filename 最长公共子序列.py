'''

如果两个字符相同 则此时最长子序列 为上一个字符的结果+1


'''

def slove(x,y):
    dp=[[0 for _ in range(len(y)+1)] for _ in range(len(x)+1)]

    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])
    return dp[-1][-1]

print(slove("abcfh","fvabngcf"))