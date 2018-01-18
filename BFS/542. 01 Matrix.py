from collections import *
class Solution(object):

    # suboptimal BFS solution.
    # take O(row * col) time complexity
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        res = [[-1 for _ in xrange(n)] for _ in xrange(m)]
        directions = [[0,1], [1,0], [0,-1],[-1,0]]
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                else:
                    dist = 0
                    q = deque()
                    q.append((i, j))
                    flag = True
                    while q:
                        for _ in xrange(len(q)):
                            row, col = q.popleft()
                            if matrix[row][col] == 0:
                                res[i][j] = dist
                                flag = False
                                break
                            else:
                                for d in directions:
                                    newRow, newCol = row + d[0], col + d[1]
                                    if 0 <= newRow < m and 0 <= newCol < n:
                                        q.append((row + d[0], col + d[1]))
                        if not flag:
                            break
                        dist += 1
        return res

    # optimized BFS solution
    # O(R * C) for both time and space complexity
    # use the previous calculate result to avoid re-adding and recomputing
    # computed results
    def updateMatrix(self, matrix):
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        q = deque()
        res = [[float('inf') for _ in xrange(n)] for _ in xrange(m)]
        directions = [[0,1], [0,-1],[1,0], [-1,0]]

        # start BFS with all of the zero cells
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                    q.append((i, j))
        while q:
            row, col = q.popleft()
            for d in directions:
                newX, newY = row + d[0], col + d[1]
                if 0 <= newX < m and 0 <= newY < n:

                    # if the neighbor's distance is smaller or equal to the dist
                    # of current cell + 1, meaning the path to this direction
                    # has a shorter path that doens't pass through the current cell
                    # so that we don't need to explore that direction from current cell

                    # else if it's greater than current cell + 1 (calculated distance
                    # from current cell), meaning that the distance could have
                    # a shorter path to the closet zero
                    # the path passing current cell is the path with shortest distance

                    if res[newX][newY] > res[row][col] + 1:
                        res[newX][newY] = res[row][col] + 1
                        q.append((newX, newY))
        return res

    # DP solution
    # O(R * C) for both time and space complexity
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return matrix
        m, n = len(matrix), len(matrix[0])
        res = [[float('inf') for _ in xrange(n)] for _ in xrange(m)]
        directions = [[0,1], [0,-1],[1,0], [-1,0]]

        # first pass : check for left and top
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    res[i][j] = 0
                else:
                    if i > 0:
                        res[i][j] = min(res[i][j], res[i - 1][j] + 1)
                    if j > 0:
                        res[i][j] = min(res[i][j], res[i][j - 1] + 1)

        # second pass : check for right and bottom
        for i in xrange(m - 1, -1, -1):
            for j in xrange(n - 1, -1, -1):
                if i < m - 1:
                    res[i][j] = min(res[i][j], res[i + 1][j] + 1)
                if j < n - 1:
                    res[i][j] = min(res[i][j], res[i][j + 1] + 1)
        return res
