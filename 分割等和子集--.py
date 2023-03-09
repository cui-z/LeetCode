'''
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，
使得两个子集的元素和相等。

注意:
每个数组中的元素不会超过 100
数组的大小不会超过 200

示例
示例 1:
输入: [1, 5, 11, 5]
输出: true
解释: 数组可以分割成 [1, 5, 5] 和 [11].

示例 2:
输入: [1, 2, 3, 5]
输出: false
解释: 数组不能分割成两个元素和相等的子集.

定义一个布尔类型的二维数组dp，数组的维度为(len(nums), target+1)，dp[i][j]的含义为数组nums[0:i+1]中是否存在一些元素，使得它们的和为j，
这里target+1的原因是需要覆盖从0到target的所有正整数。
初始情况：数组中所有元素初始化为False。dp[0]是一个长度为target+1的数组，表示nums[:1]数组中子数组的和是否可以组成j（0<=j<target），而这个数组中
只包含一个元素，其和能构成的就是nums[0]，因此将dp[0][nums[0]]填充为True。
状态转移方程。逐行逐列遍历dp数组，如何判断nums[0:i+1]中是否有子数组和是j?我们有以下几个依据：
如果nums[0:i]中有子数组和为j（也就是dp[i-1][j]的值为True），则nums[0:i+1]中一定有子数组和为j，多了一个元素而已；
如果当前新增的元素nums[i]正好等于j，那么nums[0:i+1]中一定存在子数组和为j，因为新增的这个元素nums[i]就满足条件；
3.如果当前新增的元素nums[i]小于j，那么查看一下，nums[0:i]中是否存在子数组和为target-j，也就是查看一下dp[i-1][target-j]的值是否为True；
依据以上三个条件，可以方便地写出递推关系式。


问题转换  是否有子数组和 等于target   很像 背包问题
'''

def  slove(nums):
    nums_sum = sum(nums)
    if nums_sum %2 :
        return False
    tar = nums_sum // 2
    dp=[[False for _ in range(tar+1)] for _ in range(len(nums))]
    l = nums[0]
    if l <= tar:
        dp[0][l] = True
    print(dp)
    for i in range(1,len(nums)):
        print(dp)
        for j in range(tar+1):
            if nums[i] == j or dp[i-1][j] ==True:
                dp[i][j] = True
            elif nums[i] < j:
                dp[i][j] = dp[i-1][j-nums[i]]
    return  dp[-1][-1]

print(slove([2,5,11,4]))

