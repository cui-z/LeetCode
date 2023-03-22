'''
给定不同面额的硬币（每个面额数量都很多）和一个总金额，编写一个函数可以计算凑成总金额所需
    硬币的组合数
'''


def slove(amount,coins):
    coin_len = len(coins)
    dp = [[0 for _ in range(amount + 1)] for _ in range(coin_len + 1)]

    for i in range(coin_len + 1):
        dp[i][0] = 1

    # 扫描全部coins和amount的组合
    for i in range(1, coin_len + 1):
        for j in range(1, amount + 1):
            # 如果你不把这第 i 个物品装入背包，也就是说你不使用 coins[i] 这个面值的硬币，
            # 那么凑出面额 j 的方法数 dp[i][j] 应该等于 dp[i-1][j]，继承之前的结果。
            # 如果你把这第 i 个物品装入了背包，也就是说你使用 coins[i] 这个面值的硬币，那
            # 么 dp[i][j] 应该等于 dp[i][j-coins[i-1]]
            #
            if j - coins[i - 1] >= 0:
                dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[coin_len][amount]


def slove1(amount,coins):
    dp=[0 for _ in range(amount+1)]
    dp[0]=1
    #先 遍历钱币  然后遍历总金额
    for i  in range(len(coins)):
        for a in range(1,amount+1):
            if a >= coins[i]:
                dp[a]+=dp[a-coins[i]]
    return dp[-1]




print(slove(5,[1,2,5]))
