# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid
# How many possible unique paths are there?

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # O(m * n) space complexity, 2D DP array
        path = [[1 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(1, m):
        	for j in xrange(1, n):
        		path[i][j] = path[i - 1][j] + path[i][j - 1]
        return path[-1][-1]

        # O(n) space complexity, 1D DP array
        dp = [0 for _ in xrange(n)]
        dp[0] = 1
        for i in xrange(m):
            for j in xrange(n):
                if j > 0:
                    dp[j] += dp[j - 1]
        return dp[-1]
