#给定一个M N的矩阵，按照顺时针螺旋顺序 返回所有元素

def slove(matrix):
    if len(matrix) ==1:
        return matrix[0]

    result=[]
    while len(matrix) >0:
        print("-----------------")
        result += matrix[0]
        del  matrix[0]
        print(*matrix)
        matrix = list(zip(*matrix))
        print(matrix)
        matrix.reverse()
        print(matrix)
        print("*******************")
    return result

print(slove([
    [1,2,3,6],
    [4,5,6,7],
    [7,8,9,9],
    [6,7,5,2]
]))