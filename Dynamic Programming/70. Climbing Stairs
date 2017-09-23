# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Idea is using dynamic programming
# One can reach the ith step by two ways
# 	1. taking a single step from (i - 1)th step
# 	2. taking two steps from (i - 2)th step
# so if we express a[i] to be the number of different ways to get to the ith step
# the total number of ways to reach ith is equal to sum of ways of reaching 
# (i - 1)th step and ways of reaching (i - 2)th step.
# the formula could be expressed as a[i] = a[i - 1] + a[i - 2]


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Solution 1, use three variables to dynamically update the infos
        if n <= 1 or n == 2:
        	return n
        prev, curr, result = 1, 2, 0
        for i in xrange(n - 2):
        	result = prev + curr
        	prev = curr
        	curr = result

        # Solution 2, use an array to store all the steps
        if n <= 1:
        	return 1
        dp = [0 for _ in xrange(n + 1)]
        dp[1], dp[2] = 1, 2
        for i in xrange(3, n + 1):
        	dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
