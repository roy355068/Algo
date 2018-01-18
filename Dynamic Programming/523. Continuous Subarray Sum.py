# Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

# Example 1:
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
# Example 2:
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

# Note:
# The length of the array won't exceed 10,000.
# You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        """
			The idea is to store all the sum of 1st to ith element into ith position of a new array

			then iterate from the end of the array, and check from the start to the end - 2 position
			that if any difference between the two position is the multiple of k

			Because ith element in new array means 1 + 2 + ... + ith of old array
			new[i] - new[i - n] means (n + 1) + (n + 2) + ... + i of old array, so that
			we could use this techniques to find out the continuous array that fulfill the requirement
			notice that I only need to check to the i - 2 since the continuous means "at least" 2
			elements.

        """

        # Corner cases handling
        if len(nums) < 2:
            return False
        if k == 0:
            if max(nums) == 0:
                return True
            return False

        new = [0 for _ in xrange(len(nums))]
        new[0], m = nums[0], nums[0]
        for i in xrange(1, len(nums)):
            new[i] = nums[i] + new[i - 1]
            if new[i] % k == 0:
                return True

        # Notice the boundary and negative indexation of the inner loop
        for i in xrange(len(nums) - 1, -1, -1):
            for j in xrange(i - 1):
                if j < 0:
                    continue
                if (new[i] - new[j]) % k == 0:
                    return True
        return False
       
    """
		The main idea is that (x + n*k) mod k = x ,which x can be 0, 1, ..., k-1
    """
    def mathematicalSolution(self, nums, k):
    	dic = {0: -1}
        runningSum = 0
        for i in xrange(len(nums)):
            runningSum += nums[i]
            if k != 0:
                runningSum %= k
            if runningSum in dic:
                if i - dic[runningSum] > 1:
                    return True
            else:
                dic[runningSum] = i
        return False