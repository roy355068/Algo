class Solution(object):
    def minimumTotal(self, triangle):
        # 1st solution, top-down 2d dp => time : O(N^2) space: O(N^2)
        # Given N is the total row number
        dp = [[0 for _ in xrange(row + 1)] for row in xrange(len(triangle))]
        dp[0] = [triangle[0][0]]

        for row in xrange(1, len(triangle)):
            # calculate the current row (row) from the previous row (row - 1)
            for col in xrange(row + 1):
                # if col is 0 or row, means the entry is at the edge of the row
                if col == 0:
                    dp[row][col] = triangle[row][col] + dp[row - 1][0]
                elif col == row:
                    dp[row][col] = triangle[row][col] + dp[row - 1][-1]
                # if the entry is in the middle of the row
                # take the min path
                else:
                    dp[row][col] = triangle[row][col] \
                                    + min(dp[row - 1][col], dp[row - 1][col - 1])
        return min(dp[-1])


        # 2nd solution, bottom-up 1d dp => time : O(N ^ 2) space : O(N)
        # Use a 1d dp array to store each layer's locally optimal path
        # Since row + 1 would be no longer useful when we have row
        # so we can reduce the space by using a single value to store the
        # min value comes from row + 1.
        # The dp can be visualized like this
        # --------------|
        #     ----------|
        #         ------|
        #             --|
        # each elements in dp array is the Min Sum along the path
        # after iteratively calculate the path, the minimum path Sum
        # would be the first element in the dp array
        dp = [val for val in triangle[-1]]
        for row in xrange(len(triangle) - 2, -1, -1):
            for col in xrange(row + 1):
                dp[col] = min(dp[col], dp[col + 1]) + triangle[row][col]
        return dp[0]
