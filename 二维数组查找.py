"""
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，
输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


def slove(matrix,target):
    m = len(matrix)
    n = len(matrix[0])
    i =0
    j = n-1  #初始化并不是随机初始化
    while (0 <= i <=m-1 and 0<=j <=n-1):
        curr = matrix[i][j]
        if curr == target:
            return  True
        elif curr < target:
            i+=1
        else:
            j -=1
    return False

print(slove([[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]],16))

