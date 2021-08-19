'''

给定一个二维网格和一个单词，找出单词是否在网格中

单词必须按照字母顺序 通过相邻的单元格内的字母组成 相邻是指水平相邻或者垂直相邻的单元格

zhu:
    同一个单元格内的字不能被重复使用
'''


def dfs(board, i, j, word):
    if len(word) == 0:
        return True
    if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[0]:
        return False
    board[i][j] = "*"
    res = dfs(board, i - 1, j, word[1:]) \
          or dfs(board, i + 1, j, word[1:]) \
          or dfs(board, i, j + 1, word[1:]) \
          or dfs(board, i, j - 1, word[1:])
    board[i][j] = word[0]
    return  res


def slove(board, word):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, i, j, word):
                return True
    return False

print(slove([['a','b','c','e'],
             ['s','f','c','s'],
             ['a','d','e','e']],'sec'))

