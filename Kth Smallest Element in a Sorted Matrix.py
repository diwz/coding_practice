# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# Example:

# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,

# return 13.

import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return 0

        heap = []
        row_n = len(matrix)
        col_n = len(matrix[0])

        for i in range(col_n):
            heapq.heappush(heap, (matrix[0][i], 0, i))

        for j in range(k-1):
            curr = heapq.heappop(heap)
            r = curr[1]
            c = curr[2]
            if r + 1 < row_n:
                heapq.heappush(heap, (matrix[r+1][c], r+1, c))

        return heapq.heappop(heap)[0]
