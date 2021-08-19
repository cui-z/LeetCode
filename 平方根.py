'''
计算并返回x的平方根 其中x是非负整数
返回类型时整数 结果只保留整数部分 小数部分舍去

例如 8  2
'''

def slove(x):
    left = 0
    # 为了照顾到 1 把右边界设置为 x // 2 + 1
    right = x // 2 + 1
    while left < right:
        # 注意：这里一定取右中位数，如果取左中位数，代码可能会进入死循环
        mid = left + (right - left + 1) // 2
        square = mid * mid

        if square > x:
            right = mid - 1
        else:
            left = mid
    return left
print(slove(6))