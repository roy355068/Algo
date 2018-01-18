class Solution(object):
    # Same as 200 Number of Islands
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxVal = 0
        if grid:
            row, col = len(grid), len(grid[0])
            for i in xrange(row):
                for j in xrange(col):
                    if grid[i][j] == 1:
                        maxVal = max(maxVal, self.dfs(grid, i, j))
        return maxVal

    def dfs(self, grid, i, j):
        res = 0
        if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
            # each valid island is 1 size large
            res += 1
            grid[i][j] = 0
            for diff in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                res += self.dfs(grid, i + diff[0], j + diff[1])
        return res
