"""
题目描述：给定物品的重量 weights=[1, 2, 5, 6, 7] ，对应的价值 values=[1, 6, 18, 22, 28] ， 背包能装 的最大重量为 capicity=11。
问：我们用这个背包装什么物品能获得最大价值？
注意：每件物品只有一 件。并且最终重量不能超过背包所能承载的重量。
"""


def slove(weights,values,capicity):
    dp = [[0 for _ in range(capicity+1)] for _ in range(len(weights)+1)]

    for i  in range(len(weights)):
        for j in range(1,capicity+1):
            if weights[i] > j:
                dp[i+1][j] = dp[i][j]
            else:
                dp[i+1][j] = max(dp[i][j],dp[i+1][j-weights[i]]+values[i])
    print(dp)
    return dp[-1][-1]

print(slove([1, 2, 5, 6, 7],[1, 6, 18, 22, 28],8))
