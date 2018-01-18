class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []

        self.dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = []
        m, n = len(matrix), len(matrix[0])
        # use two different lists to label if each cell is reachable
        # to the two seas
        pVisited = [[False for _ in xrange(n)] for _ in xrange(m)]
        aVisited = [[False for _ in xrange(n)] for _ in xrange(m)]
        minVal = float('-inf')
        # run dfs for left and right border
        for i in xrange(m):
            self.dfs(matrix, i, 0, pVisited, minVal)
            self.dfs(matrix, i, n - 1, aVisited, minVal)
        # run dfs for up and down border
        for j in xrange(n):
            self.dfs(matrix, 0, j, pVisited, minVal)
            self.dfs(matrix, m - 1, j, aVisited, minVal)
        # if the cell can reach both the Pacific and Atlantic oceans
        # append the coordination into res
        for i in xrange(m):
            for j in xrange(n):
                if pVisited[i][j] and aVisited[i][j]:
                    res.append([i, j])
        return res

    def dfs(self, matrix, i, j, visited, height):
        # we start the dfs from border into the center of the matrix
        # so if the height in the current cell is higher than the "inner" one
        # will result in blocking the water, hence directly return the recursion call
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or visited[i][j] or height > matrix[i][j]:
            return
        visited[i][j] = True
        for d in self.dir:
            self.dfs(matrix, i + d[0], j + d[1], visited, matrix[i][j])
