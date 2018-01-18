# Given a non-empty array containing only positive integers, 
# find if the array can be partitioned into two subsets 
# such that the sum of elements in both subsets is equal.

# Note:
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# Example 1:

# Input: [1, 5, 11, 5]

# Output: true

# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:

# Input: [1, 2, 3, 5]

# Output: false

# Explanation: The array cannot be partitioned into equal sum subsets.


# knapsack problem
class Solution(object):

	def towDArrayWay(self, nums):
		s = sum(nums)
        if s == 0 or s % 2 != 0:
            return False
        s /= 2
        dp = [[True if x == 0 else False for x in xrange(s + 1)] for _ in xrange(len(nums) + 1)]
        for i in xrange(1, len(nums) + 1):
            for j in xrange(1, s + 1):
                if j >= nums[i - 1]:
                    # see if j can be achievable by not taking the current number (dp[i - 1][j])
                    # or by taking the current number (dp[i - 1][j - nums[i - 1]])
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
        return dp[-1][-1]

    # 1D DP array solution
	def canPartition(self, nums):
		""" rtype = boolean """
		if not nums:
			return True
		s = sum(nums)

		# The problem is if we can partition the array into two arrays that has the same sums
		# so if the sum of the whole array is not even, return False directly
		if s % 2 != 0:
			return False

		# the idea is to find if there's subsequence that can composed of sum / 2
		# so divide the sum by 2
		s /= 2

		# construct an list for every numbers from 0 to sum
		# The first element is always True (because 0 can be composed of itsself (doesn't
		# take anything from the array))
		dp = [False for _ in xrange(s + 1)]
		dp[0] = True

		# Every loop of nums refreshes dp array. 
		# We might get dp[i] from dp[i-num] whose index is smaller than i. 
		# If we increase the index of sum from 0 to sum, we will get dp[i] from dp[i-num],
		# while dp[i-num] has been updated in this loop. 
		# This dp[i-num] is not the number we got from the previous loop.
		for num in nums:

			for i in xrange(s, -1, -1):
				if i >= num:
					# dp[i] = dp[i] or dp[i - num]
					"""
					The meaning of this sentence is, I can choose not pick the current num (dp[i])
					or pick the current number (dp[i - num]) and see if I can get to the
					current number i by doing either actions.
					"""
					"""
						如果inner loop是順向，則dp[i - num]會取到在內迴圈裡先前已被更新的dp[i]
						所以就不會是上一輪外迴圈更新的dp array，而是內回圈又更新後的結果
						代表會允許程式對nums裡的數字重複取直，但在本題，一個數字只能使用一次時就只能由
						逆向走，如此一來就確保一定是取道由外迴圈更新的dp
					"""
					dp[i] = dp[i] or dp[i - num]
		# return the last item in the array since it is indicating if we can get to the 
		# sum in the array
		return dp[-1]