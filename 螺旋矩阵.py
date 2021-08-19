#给定一个M N的矩阵，按照顺时针螺旋顺序 返回所有元素

def slove(matrix):
    if len(matrix) ==1:
        return matrix[0]

    result=[]
    while len(matrix) >0:
        result += matrix[0]
        del  matrix[0]
        matrix = list(zip(*matrix))
        matrix.reverse()
    return result

print(slove([
    [1,2,3],
    [4,5,6],
    [7,8,9]
]))