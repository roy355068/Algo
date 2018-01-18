class Solution(object):

    # Time complexity : O(numRows ^ 2)
    # Space complexity : O(numRows ^ 2)
    # Since needs to go through every element in the res
    def pascalI(self, numRows):
        res = [[1 for _ in xrange(i)] for i in xrange(1, numRows + 1)]
        for row in xrange(2, numRows):
            for col in xrange(1, row):
                res[row][col] = res[row - 1][col - 1] + res[row - 1][col]
        return res

    # Time complexity : O(rowIndex ^ 2)
    # Space complexity : O(rowIndex)
    def pascalII(self, rowIndex):
        dp = [0 for _ in xrange(rowIndex + 1)]
        dp[0] = 1
        for i in xrange(1, rowIndex + 1):
            # Inner loop start from the back and move forward
            # In this way, we can assure that the dp[j] is really updated
            # by itself and its previous element dp[j - 1]

            # Otherwise if we start from the beginning and work to the back
            # the value would propagate and affect all value behind it
            for j in xrange(i, 0, -1):
                dp[j] += dp[j - 1]
        return dp
