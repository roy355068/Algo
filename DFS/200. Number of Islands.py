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

# Using DFS, find the block that has land, then use dfs to "visit" (change all the connecting lands)
# other lands on the same island and set the block to zero (visited)
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
        	return 0
        res = 0
        for i in xrange(len(grid)):
        	for j in xrange(len(grid[0])):
        		if grid[i][j] == "1":
        			self.dfs(grid, i, j)
        			res += 1
        return res

    def dfs(self, g, i, j):
    	if i < 0 or j < 0 or i > len(g) - 1 or j > len(g[0]) - 1 or g[i][j] != "1":
    		return
    	g[i][j] = "0"
    	self.dfs(g, i + 1, j)
    	self.dfs(g, i - 1, j)
    	self.dfs(g, i, j + 1)
    	self.dfs(g, i, j - 1)