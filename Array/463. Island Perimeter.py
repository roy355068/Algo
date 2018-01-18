class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row, col = len(grid), len(grid[0])
        res = 0
        for i in xrange(row):
            for j in xrange(col):
                if grid[i][j] == 1:
                    res += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        res -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        res -= 2
        return res
