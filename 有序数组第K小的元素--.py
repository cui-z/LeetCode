"""
给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。

示例：
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
返回 13。
"""

# 解题思路  https://codeantenna.com/a/E7qjaUa7ir

def kthSmallest(matrix, k):
    n = len(matrix)
    minn = matrix[0][0]
    maxx = matrix[n-1][n-1]

    #这个函数的功能是，返回matrix小于等于target的数的个数
    #从左下角开始找。
    def calculate(target):
        #计数
        cnt = 0
        #初始的位置，x为行数，y为列数
        x = n-1
        y = 0
        while 0 <= x < n and 0 <= y < n:
            if matrix[x][y] <= target:
                cnt += x+1
                y += 1
            else:
                x -= 1
        return cnt

    #对数值开始二分查找
    left = minn
    right = maxx
    while left < right:
        mid = left + (right-left)//2
        if calculate(mid) >= k:
            right = mid
        #需要向右压缩，因为calculate(mid)<k，则mid可能不是答案
        #若大于k，则mid可能为答案，因为可能存在多个mid这个值
        else:
            left = mid + 1
    return left