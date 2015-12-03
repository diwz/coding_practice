# Given an integer n, generate a square matrix filled with elements from 1 to
# n^2 in spiral order.

# For example,
# Given n = 3,

# You should return the following matrix:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for i in range(n)]
        left, right, top, bottom = 0, n-1, 0, n-1
        num = 1
        while left <= right and top <= bottom:
            for i in range(left, right+1):
                matrix[top][i] = num
                num += 1
            for i in range(top+1, bottom):
                matrix[i][right] = num
                num += 1
            for i in range(right, left-1, -1):
                if top < bottom:
                    matrix[bottom][i] = num
                    num += 1
            for i in range(bottom-1, top, -1):
                if left < right:
                    matrix[i][left] = num
                    num += 1
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return matrix
