"""
给定一个 n × n 的二维矩阵表示一个图像。

将图像顺时针旋转 90 度。

说明：

你必须在原地旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要使用另一个矩阵来旋转图像。

示例 1:

给定 matrix =
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
"""

def slove(matrix):
    #先对角线旋转 再左右旋转
    m=len(matrix)
    n=len(matrix[0])

    for i in range(m):
        for j in range(n):
            if j>i:
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
    for i in range(m):
        for j in range(m//2):
            matrix[i][j],matrix[i][m-j-1]=matrix[i][m-j-1],matrix[i][j]
    return matrix

print(slove([
  [1,2],
  [4,5]
]))