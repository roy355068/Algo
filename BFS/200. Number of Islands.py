import collections
class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        res = 0
        m, n = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # traverse each grid, visit the neighbors of
        # each grid when traversing the 2d array
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j] == "1":
                    res += 1
                    grid[i][j] = "0"
                    q = collections.deque()
                    q.append([i, j])
                    while q:
                        row, col = q.popleft()
                        # same as 490. The Maze.
                        # once pick a directions, we need to move toward that
                        # direction until we hit a wall (sea in this case)
                        # and visit the grids along the way
                        for d in directions:
                            newRow, newCol = row + d[0], col + d[1]
                            # if the boundary and value check of the grid are both valid
                            # push the coordination into queue and visit the grid
                            if 0 <= newRow < m and 0 <= newCol < n and grid[newRow][newCol] == "1":
                                q.append([newRow, newCol])
                                grid[newRow][newCol] = "0"
        return res


        
