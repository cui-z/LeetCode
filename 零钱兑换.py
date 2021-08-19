'''
给定不同面额的硬币（每个面额数量都很多）和一个总金额，编写一个函数可以计算凑成总金额所需
    最少的硬币的个数
'''

#float('inf')  无穷大
def slove(coins,target):
    result=[float('inf')]*(target+1)

    for t in target:
        for c in coins:
            if t>c:
                result[t] = min(result[t-c]+1,result[t])
    return  result[-1] if result[-1] != float('inf') else -1