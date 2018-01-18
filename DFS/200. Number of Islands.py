# Using DFS, find the block that has land, then use dfs to "visit" (change all the connecting lands)
# other lands on the same island and set the block to zero (visited)
# O(M * N) for both time and space complexity
# Worst case for space when the grid is filled with lands where DFS goes
# M * N deep
from collections import *
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    res += 1
        return res

    def dfs(self, g, i, j):
        if 0 <= i < len(g) and 0 <= j < len(g[0]) and g[i][j] == "1":
            g[i][j] = "0"
            for diff in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                self.dfs(g, i + diff[0], j + diff[1])

    # BFS solution
    def numIslands(self, grid):
        if not grid:
            return 0
        res = 0
        q = deque()
        q.append((0, 0))
        while q:
            
