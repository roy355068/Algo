# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]

# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3


# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function. (So time complexity would be a big issue)

# Idea is using DP to store the sum from 0 to i in the ith element of array
# and use the subtraction property to calculate the cumulative sum in a certain range
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.t = nums
        for i in xrange(1, len(nums)):
        	self.t[i] += self.t[i - 1]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
        	return self.t[j]
        return self.t[j] - self.t[i - 1]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)