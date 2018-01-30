class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        res = 0
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # traverse each grid
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                # if the grid is a island, dfs traverse its neighbors
                # and set the connected land as visited (set to zero)
                # to avoid double count
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    # after visiting all connected lands, increment the
                    # island number by one
                    res += 1
        return res

    def dfs(self, grid, i, j):
        # boundary checking
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return
        # visit current grid
        grid[i][j] = "0"
        for d in self.directions:
            self.dfs(grid, i + d[0], j + d[1])
