from collections import *

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        x, y = click[0], click[1]
        if board[x][y] == "M":
            board[x][y] = "X"
        else:
            self.update(board, x, y)
        return board

    def update(self, board, x, y):
        q = deque()
        q.append((x, y))

        while q:
            curr = q.popleft()
            row, col = curr[0], curr[1]

            mineCount = self.mineCounter(board, row, col)
            if mineCount != 0:
                board[row][col] = str(mineCount)
            else:
                board[row][col] = "B"
                for i in xrange(-1, 2):
                    for j in xrange(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        newX, newY = row + i, col + j
                        if 0 <= newX < len(board) and 0 <= newY < len(board[0]) and board[newX][newY] == "E":
                            board[newX][newY] = "B"
                            q.append((newX, newY))

    def mineCounter(self, board, x, y):
        count = 0
        for i in xrange(-1, 2):
            for j in xrange(-1, 2):
                newX, newY = x + i, y + j
                if 0 <= newX < len(board) and 0 <= newY < len(board[0]) and \
                    board[newX][newY] == "M":
                    count += 1
        return count
