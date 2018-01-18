class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # use index to indicate the amount of money, so we need to have index "amount"
        dp = [0 for _ in xrange(amount + 1)]
        # i right now is the indices as well as amount of money
        for i in xrange(1, len(dp)):
            # minNumCoin is the least amount of coins that is needed to combine into
            # current amount : i
            # Here we start to search all coins to found out the least amount of coin
            # Based on the DP formula :
            # Suppose we have coins, [2, 3, 5], we could know that any given amount of money
            # could composed of 2, 3, or 5 if the amount is greater or equal to the value of a coin

            # dp[i] = min(dp[i - 2], dp[i - 3], dp[i - 5]) + 1
            # minNumCoin could reduce the amount of accessing array's element though
            # accessing should only have O(1) time complexity
            minNumCoin = float('inf')
            for c in coins:
                if c <= i:
                    minNumCoin = min(minNumCoin, dp[i - c] + 1)
            dp[i] = minNumCoin
        return dp[-1] if dp[-1] != float('inf') else -1
