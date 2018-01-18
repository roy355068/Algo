# Given a m x n grid filled with non-negative numbers, 
# find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

class Solution(object):
	def minPathSum(self, grid):
		if not grid:
			return 0
		for i in xrange(len(grid)):
			for j in xrange(len(grid[0])):
				if i == 0 and j == 0:
					continue
				elif i == 0:
					grid[i][j] = grid[i][j - 1]
				elif j == 0:
					grid[i][j] = grid[i - 1][j]
				else:
					grid[i][j] = min(grid[i][j - 1], grid[i - 1][j])
		return grid[-1][-1]