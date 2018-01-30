class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        m, n = len(maze), len(maze[0])
        destX, destY = destination[0], destination[1]

        # Keep track of the shortest dist from start to each cell
        distance = [[float('inf') for _ in xrange(n)] for _ in xrange(m)]

        # starting point's dist is zero by definition
        distance[start[0]][start[1]] = 0
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.dfs(maze, start, distance, m, n)

        return -1 if distance[destX][destY] == float('inf') else distance[destX][destY]

    def dfs(self, maze, point, dist, m, n):
        for d in self.directions:
            x, y = point[0], point[1]
            # count # of steps in this direction until hit the wall
            count = 0
            while 0 <= x < m and 0 <= y < n and maze[x][y] == 0:
                x += d[0]
                y += d[1]
                count += 1
            x -= d[0]
            y -= d[1]
            count -= 1
            # if the dist from start + count is less than the original dist in the cell
            # update it and start next round of dfs from here (potential candidate for
            # finding shortest path)
            if dist[x][y] > dist[point[0]][point[1]] + count:
                dist[x][y] = dist[point[0]][point[1]] + count
                self.dfs(maze, [x, y], dist, m, n)
