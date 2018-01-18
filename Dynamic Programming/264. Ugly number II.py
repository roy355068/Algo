# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

# Note that 1 is typically treated as an ugly number, and n does not exceed 1690

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1 for _ in xrange(n)]
        t2, t3, t5 = 0, 0, 0
        for i in xrange(1, n):
        	dp[i] = min(dp[t2] * 2, dp[t3] * 3, dp[t5] * 5)
        	if dp[i] == dp[t2] * 2:
        		t2 += 1
        	if dp[i] == dp[t3] * 3:
        		t3 += 1
        	if dp[i] == dp[t5] * 5:
        		t5 += 1
        return dp[n - 1]