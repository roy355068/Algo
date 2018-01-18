class Solution(object):

    # O(M * N) for both time and space complexity
    # The idea is that the element [i][j] in dp array is determine by
    # element of [i - 1][j - 1], [i][j - 1], [i - 1][j] and the state of itself
    # if any one of these four blocks is not 1 then no square can forms
    # O(M * N) for both time and space complexity
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        maxLen = 0
        dp = [[0 for _ in xrange(len(matrix[0]) + 1)] for _ in xrange(len(matrix) + 1)]
        for i in xrange(1, len(dp)):
            for j in xrange(1, len(dp[0])):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1
                    maxLen = max(maxLen, dp[i][j])
        return maxLen ** 2

    # Slightly Optimized solution, only use two arrays to
    # store the prev and curr status of the dp
    # Reduced space complexity to O(N)
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        prev = [0] * m
        curr = [0] * m
        maxLen = 0
        for row in xrange(m):
            prev[row] = int(matrix[row][0])
            maxLen = max(maxLen, prev[row])

        for col in xrange(1, n):
            curr[0] = int(matrix[0][col])
            maxLen = max(maxLen, curr[0])
            for row in xrange(1, m):
                if matrix[row][col] == "1":
                    curr[row] = min(curr[row - 1], prev[row], prev[row - 1]) + 1
                    maxLen = max(maxLen, curr[row])
            prev = curr
            curr = [0] * m
        return maxLen ** 2

    # Further optimized from solution 2
    # only need one O(N) array to represent curr col
    # and one variable to record the element in the top-left position
    # in the previous column
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])

        dp = [0] * (n + 1)
        maxLen = 0
        prevTopLeft = 0

        for i in xrange(m):
            for j in xrange(1, n + 1):
                # store the original value of dp[j] and serve it as
                # prevTopLeft in the next round of iteration because we're
                # going to change dp[j] and the unwanted result will
                # propagate if we don't keep the original value
                temp = dp[j]
                if matrix[i][j - 1] == "1":
                    # take the element from left, top and previous top left
                    # and find the min val among these three element and update
                    dp[j] = min(dp[j], dp[j - 1], prevTopLeft) + 1
                    maxLen = max(maxLen, dp[j])
                else:
                    dp[j] = 0
                # assign back the original dp[j] to prevTopLeft to avoid
                # polluting the latter elements with previous data in dp process
                prevTopLeft = temp
        return maxLen ** 2
