# Write a program to solve a Sudoku puzzle by filling the empty cells.
# Empty cells are indicated by the character '.'.
# You may assume that there will be only one unique solution.


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if board is None or len(board[0]) == 0:
            return

        def isValid(x, y):
            tmp = board[x][y]
            board[x][y] = "."
            for i in range(9):
                if board[i][y] == tmp:
                    return False
            for i in range(9):
                if board[x][i] == tmp:
                    return False
            for i in range(3):
                for j in range(3):
                    if board[(x//3)*3+i][(y//3)*3+j] == tmp:
                        return False
            board[x][y] = tmp
            return True

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == ".":
                        for k in "123456789":
                            board[i][j] = k
                            if isValid(i, j) and solve(board):
                                return True
                            board[i][j] = "."
                        return False
            return True

        solve(board)
