from collections import *

class Solution(object):
	def theMaze(self, maze, start, dest):
		# initialization
		m, n = len(maze), len(maze[0])
		q = deque()
		q.append(start)
		visited = [[False for _ in xrange(n)] for _ in xrange(m)]
		visited[start[0]][start[1]] = True
		directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

		# BFS
		while q:
			# pop the queue
			curr = q.popleft()
			if curr == dest:
				return True

			x, y = curr[0], curr[1]
			for d in directions:
				# newX, newY are the stopping point
				newX, newY = self.roll(maze, x, y, m, n, d)
				# if not visited, enqueue the point for following visits
				# and (pre)visit the cell
				if not visited[newX][newY]:
					visited[curr[0]][curr[1]] = True
					q.append([newX, newY])
		return False

	# helper function. roll the ball until hits the wall
	# return the stopping position
	def roll(self, maze, x, y, m, n, d):
		while 0 <= x < m and 0 <= y < n and maze[x][y] == 0:
			x += d[0]
			y += d[1]
		# because the iteration above will push the ball to invalid position
		# so we have to move back to valid point
		x -= d[0]
		y -= d[1]
		return (x, y)