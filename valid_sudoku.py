# Determine if a Sudoku is valid
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if len(board) != 9 or len(board[0]) != 9:
            return False

        for row in board:
            if not self.validate(row):
                return False

        for i in range(9):
            col = [board[j][i] for j in range(9)]
            if not self.validate(col):
                return False

        for i in (0, 3, 6):
            for j in (0, 3, 6):
                sq = [board[i+m][j+n] for m in (0, 1, 2) for n in (0, 1, 2)]
            if not self.validate(sq):
                return False

        return True

    def validate(self, str_list):
        return str_list.count('.') + len(set(str_list)) - 1 == 9
