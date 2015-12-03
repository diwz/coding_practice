# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# For example,
# Given the following matrix:

# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return res
        left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1
        while left <= right and top <= bottom:
            for i in range(left, right+1):
                res.append(matrix[top][i])
            for i in range(top + 1, bottom):
                res.append(matrix[i][right])
            for i in range(right, left-1, -1):
                if top < bottom:
                    res.append(matrix[bottom][i])
            for i in range(bottom-1, top, -1):
                if left < right:
                    res.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1

        return res
