'''
子序列会了 淄子串就简单了  子串连续

'''

def slove(x,y):
    dp = [[0 for _ in range(len(y)+1)] for _ in range(len(x)+1)]
    result = 0
    res=""
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i]==y[j]:
                dp[i+1][j+1] = dp[i][j]+1
                print(dp[i+1][j+1])
                if dp[i+1][j+1] > result:
                    result = dp[i+1][j+1]
                    res = x[i+1-result:i+1]
            else:
                dp[i+1][j+1] = 0
    return result,res

print(slove("abc","dgeabl"))