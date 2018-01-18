class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        res = 0
        if not matrix:
            return res

        m, n = len(matrix), len(matrix[0])
        # cache up the computed results to avoid repetitive computation
        cache = [[-1 for _ in xrange(n)] for _ in xrange(m)]
        self.dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in xrange(m):
            for j in xrange(n):
                # or we can do it in the opposite way => find the strictly
                # decreasing path
                # length = self.dfs(matrix, i, j, cache, float('inf'))
                length = self.dfs(matrix, i, j, cache, float('-inf'))
                res = max(res, length)
        return res

    def dfs(self, matrix, i, j, cache, prev):
        # if we decide to find the decreasing path then we need to alter the last condition
        # if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] >= prev:
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] <= prev:
            return 0
        if cache[i][j] != -1:
            return cache[i][j]
        res = 1
        for d in self.dir:
            currMax = 1 + self.dfs(matrix, i + d[0], j + d[1], cache, matrix[i][j])
            res = max(res, currMax)
        cache[i][j] = res
        return res
