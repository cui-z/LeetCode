"""
是将n个皇后放置在n*n的棋盘上，皇后彼此之间不能相互攻击(任意两个皇后不能位于同一行，同一列，同一斜线)。

给定一个整数n，返回所有不同的n皇后问题的解决方案。每个解决方案包含一个明确的n皇后放置布局，其中“Q”和“.”分别表示一个女王和一个空位置。

样例1:输入:1
输出:
 [["Q"]]

 样例2:输入:4
输出:
[
 // Solution 1
  [".Q..",
 "...Q",
 "Q...",
 "..Q."
  ],
 // Solution 2
  ["..Q.",
 "Q...",
 "...Q",
 ".Q.."
  ]
]


回溯法可解决
"""

def solveNQueens(n) :
    if not n: return []
    board = [['.'] * n for _ in range(n)]
    res = []
    def isVaild(board,row, col):
        #判断同一列是否冲突
        for i in range(len(board)):
            if board[i][col] == 'Q':
                return False
        # 判断左上角是否冲突
        i = row -1
        j = col -1
        while i>=0 and j>=0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # 判断右上角是否冲突
        i = row - 1
        j = col + 1
        while i>=0 and j < len(board):
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

    def backtracking(board, row, n):
        # 如果走到最后一行，说明已经找到一个解
        if row == n:
            temp_res = []
            for temp in board:
                temp_str = "".join(temp)
                temp_res.append(temp_str)
            res.append(temp_res)
            return
        for col in range(n):
            if isVaild(board, row, col):
                board[row][col] = 'Q'
                backtracking(board, row+1, n)
                board[row][col] = '.'
            else:
                pass
            # if not isVaild(board, row, col):
            #     continue
            # board[row][col] = 'Q'
            # backtracking(board, row+1, n)
            # board[row][col] = '.'
    backtracking(board, 0, n)
    return res


print(solveNQueens(4))