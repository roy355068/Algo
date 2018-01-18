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
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] != "E":
            return

        mineNum = self.mineCounter(board, x, y)
        if mineNum > 0:
            board[x][y] = str(mineNum)
        else:
            board[x][y] = "B"
            for i in xrange(-1, 2):
                for j in xrange(-1, 2):
                    self.update(board, x + i, y + j)

    def mineCounter(self, board, x, y):
        count = 0
        for i in xrange(-1, 2):
            for j in xrange(-1, 2):
                newX, newY = x + i, y + j
                if 0 <= newX < len(board) and 0 <= newY < len(board[0]) and \
                    board[newX][newY] == "M":
                    count += 1
        return count
