class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        res = []
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        aVisited = [[False for _ in xrange(n)] for _ in xrange(m)]
        pVisited = [[False for _ in xrange(n)] for _ in xrange(m)]
        pQ = collections.deque()
        aQ = collections.deque()

        for i in xrange(m):
            aVisited[i][n - 1] = True
            pVisited[i][0]     = True
            pQ.append([i, 0])
            aQ.append([i, n - 1])

        for j in xrange(n):
            aVisited[m - 1][j] = True
            pVisited[0][j]     = True
            pQ.append([0, j])
            aQ.append([m - 1, j])

        self.bfs(matrix, pVisited, pQ)
        self.bfs(matrix, aVisited, aQ)

        for i in xrange(m):
            for j in xrange(n):
                if pVisited[i][j] and aVisited[i][j]:
                    res.append([i, j])
        return res

    def bfs(self, matrix, visited, q):
        m, n = len(matrix), len(matrix[0])
        while q:
            curr = q.popleft()
            for d in self.directions:
                x, y = curr[0], curr[1]
                newX, newY = x + d[0], y + d[1]
                if 0 <= newX < m and 0 <= newY < n and not visited[newX][newY] and matrix[x][y] <= matrix[newX][newY]:
                    visited[newX][newY] = True
                    q.append([newX, newY])

                    
