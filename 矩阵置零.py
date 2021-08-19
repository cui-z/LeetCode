'''
给定一个m n的矩阵  如果有一个元素为0  则其所在的行和列都为0
'''

def slove(matrix):
    l_set=set()
    w_set=set()
    for j in range(len(matrix)):
        for k in range(len(matrix[j])):
            if matrix[j][k] == 0:
                l_set.add(k)
                w_set.add(j)
    for w in w_set:
        for k in range(len(matrix[0])):
            matrix[w][k]=0
    for j in range(len(matrix)):
        for l in l_set:
            matrix[j][l] = 0
    return matrix

print(slove([
    [1,1,1],
    [1,0,1],
    [1,1,1]
]))