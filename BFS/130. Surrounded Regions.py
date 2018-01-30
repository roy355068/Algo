class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        q = collections.deque()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in xrange(m):
            for j in xrange(n):
                # put the "O"s on the borders for BFS
                if (i in [0, m - 1] or j in [0, n - 1]) and board[i][j] == "O":
                    q.append([i, j])

        # temporary label the "O"s conneted to borders as "T" and restore it back later
        while q:
            x, y = q.popleft()
            board[x][y] = "T"
            for d in directions:
                newX, newY = x + d[0], y + d[1]
                if 0 <= newX < m and 0 <= newY < n and board[newX][newY] == "O":
                    q.append([newX, newY])

        for i in xrange(m):
            for j in xrange(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
