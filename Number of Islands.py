# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# 11110
# 11010
# 11000
# 00000
# Answer: 1

# Example 2:

# 11000
# 11000
# 00100
# 00011
# Answer: 3
#

class Solution(object):
    def explore(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] is '0':
            return
        grid[i][j] = '0'
        self.explore(grid, i-1, j)
        self.explore(grid, i+1, j)
        self.explore(grid, i, j-1)
        self.explore(grid, i, j+1)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        g = []
        for i in range(len(grid)):
            g.append(list(grid[i]))
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if g[i][j] is '1':
                    count += 1
                    self.explore(g, i, j)
        return count

sol = Solution()
print sol.numIslands(["11000","11000","00100","00011"])
