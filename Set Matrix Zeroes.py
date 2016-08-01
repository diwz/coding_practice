# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

# Follow up:
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return
        zeroInFirstCol = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                zeroInFirstCol = True
                break
        zeroInFirstRow = False
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                zeroInFirstRow = True
                break
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if zeroInFirstCol:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if zeroInFirstRow:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
