class Solution(object):
    def numSquares(self, n):
        if n <= 0:
            return 0
        count = [float('inf') for _ in xrange(n + 1)]
        count[0] = 0
        for i in xrange(1, n + 1):
            j = 1
            while j * j <= i:
                # for each i, it must be the sum of a perfect square (j * j)
                # and some other number i - (j * j)
                count[i] = min(count[i], count[i - (j * j)] + 1)
                j += 1
        return count[-1]

    # Static DP for improving the performance if
    # we need to call the method for many times
    dp = [0]
    def numSquares(self, n):
        dp = self.dp
        while len(dp) <= n:
            m = len(dp)
            minCount = float('inf')
            j = 1
            while j * j <= m:
                minCount = min(minCount, dp[m - (j * j)] + 1)
                j += 1
            dp.append(minCount)
        return dp[n]
