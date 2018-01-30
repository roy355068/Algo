from heapq import *
class Solution(object):

    # Regular BFS
    # time : O(m * n * max(m, n))
    # space : O(m * n)
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        m, n = len(maze), len(maze[0])
        dX, dY = destination[0], destination[1]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # min distance from starting point to each cell
        distance = [[float('inf') for _ in xrange(n)] for _ in xrange(m)]
        # the dist b/t starting point and itself is zero
        distance[start[0]][start[1]] = 0
        q = collections.deque()
        q.append(start)

        while q:
            curr = q.popleft()
            for d in directions:
                x, y = curr[0], curr[1]
                # count is the dist that the ball needs to travel in that direction
                count = 0
                while 0 <= x < m and 0 <= y < n and maze[x][y] != 1:
                    x += d[0]
                    y += d[1]
                    count += 1

                x -= d[0]
                y -= d[1]
                count -= 1

                # if the dist from starting point via other path is larger than
                # the previous point + count, then update the dist in that cell
                if distance[x][y] > distance[curr[0]][curr[1]] + count:
                    distance[x][y] = distance[curr[0]][curr[1]] + count
                    q.append([x, y])
        # check if the destination is reachable
        return -1 if distance[dX][dY] == float('inf') else distance[dX][dY]

    # Dijkstra's algorithm
    def shortestDistance(self, maze, start, dest):
        m, n = len(maze), len(maze[0])
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # initialize the distance from starting point to each cell as inf
        distance = [[float('inf') for _ in xrange(n)] for _ in xrange(m)]
        distance[start[0]][start[1]] = 0
        self.dijkstra(maze, start, distance, m, n)
        return -1 if distance[dest[0]][dest[1]] == float('inf') else distance[dest[0]][dest[1]]

    def dijkstra(self, maze, start, distance, m, n):
        q = []
        heappush(q, (0, start[0], start[1]))
        while q:
            # extractMin()
            curr = heappop(q)
            # if there's already a shorter path than starting from current x, y
            if distance[curr[1]][curr[2]] < curr[0]:
                continue

            # roll to the four directions til hit the wall
            for d in self.directions:
                x, y = curr[1], curr[2]
                count = 0
                while 0 <= x < m and 0 <= y < n and maze[x][y] == 0:
                    x += d[0]
                    y += d[1]
                    count += 1
                x -= d[0]
                y -= d[1]
                count -= 1

                # if start from curr cell could result in shorter path, update it
                if distance[x][y] > distance[curr[1]][curr[2]] + count:
                    distance[x][y] = distance[curr[1]][curr[2]] + count
                    heappush(q, (distance[x][y], x, y))
