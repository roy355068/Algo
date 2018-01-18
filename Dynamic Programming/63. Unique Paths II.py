class Solution(object):
	def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        path = [[1 for _ in xrange(len(obstacleGrid[0]))] for _ in xrange(len(obstacleGrid))]
        if len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1 and obstacleGrid[0][0] == 1:
            return 0
        for i in xrange(1, len(obstacleGrid)):
            path[i][0] = 0 if obstacleGrid[i - 1][0] == 1 or obstacleGrid[i][0] == 1 else path[i - 1][0]
        for j in xrange(1, len(obstacleGrid[0])):
            path[0][j] = 0 if obstacleGrid[0][j - 1] == 1 or obstacleGrid[0][j] == 1 else path[0][j - 1]

        for i in xrange(1, len(obstacleGrid)):
            for j in xrange(1, len(obstacleGrid[0])):
                if obstacleGrid[i - 1][j] == 1 and obstacleGrid[i][j - 1] == 1:
                    path[i][j] = 0
                elif obstacleGrid[i - 1][j] == 1:
                    path[i][j] = path[i][j - 1]
                elif obstacleGrid[i][j - 1] == 1:
                    path[i][j] = path[i - 1][j]
                else:
                    path[i][j] = path[i - 1][j] + path[i][j - 1] if obstacleGrid[i][j] == 0 else 0
        return path[-1][-1]

    #       dp[j] = dp[j] + dp[j - 1]
    # means new dp[j] = old dp[j] + dp[j - 1]
    # means current cell = top cell + left cell
    def uniquePathsWithObstacles(self, obstacleGrid):
    	m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for _ in xrange(n)]
        dp[0] = 1
        for i in xrange(m):
            for j in xrange(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif obstacleGrid[i][j] == 0 and j > 0:
                    dp[j] += dp[j - 1]
        return dp[-1]
