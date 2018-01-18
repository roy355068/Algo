class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])

        for r in xrange(m):
            for c in xrange(n):
                count = 0
                for i in xrange(-1, 2):
                    for j in xrange(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        count += self.helper(board, r + i, c + j)
                if board[r][c] == 1 and count in (2, 3):
                    board[r][c] = 3
                elif board[r][c] == 0 and count == 3:
                    board[r][c] = 2

        for i in xrange(m):
            for j in xrange(n):
                board[i][j] >>= 1

    def helper(self, b, i, j):
        if i < 0 or j < 0 or i > len(b) - 1 or j > len(b[0]) - 1:
            return 0
        return board[i][j] & 1
