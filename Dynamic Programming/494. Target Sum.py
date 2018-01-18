# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. 
# Now you have 2 symbols + and -. For each integer, 
# you should choose one from + and - as its new symbol.

# Find out how many ways to assign symbols to make sum of integers equal to target S.

# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 

# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3

# There are 5 ways to assign symbols to make the sum of nums be target 3.
# Note:
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.

class Solution(object):
	""" Since the operations we allowed to use are + and -, so we could define two groups
	 the positive group and negative group. Using some algebra, we can derive the formula :

	 				   sum(P) - sum(N) = target
	 sum(P) + sum(N) + sum(P) - sum(N) = target + sum(P) + sum(N)
	 						2 * sum(P) = target + sum(nums)

	Then the job would be find the number of subsequences P that satisfies
								sum(P) = (target + sum(nums)) / 2
	which will make the problem into an "Partition Equal Subset Sum" question like 416 in LeetCode
	"""
	def findTargetSumWays(self, nums, S):
        sumOfNums = sum(nums)
        return 0 if sumOfNums < S or (sumOfNums + S) % 2 != 0 else self.findSubSet(nums, (sumOfNums + S)/2)

    """
	dp[0] = 1 because one of the initial ways to generate 0 is not picking anything
	dp[i] += dp[i - num] means sum up the ways of adding up to s (pick current num or not)
    """
    def findSubSet(self, nums, target):
        dp = [0 for _ in xrange(target + 1)]
        dp[0] = 1
        for num in nums:
        	"""
        	Why start from right instead of left in the nested loop?
        	because i - num would 

        	"""
            for i in xrange(target, num - 1, -1):
                    dp[i] = dp[i] + dp[i - num]
        return dp[target]
