# Given an array S of n integers, find three integers in S such that the sum is closest to a 
# given number, target. Return the sum of the three integers. 
# You may assume that each input would have exactly one solution.

#     For example, given array S = {-1 2 1 -4}, and target = 1.
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = nums[0] + nums[1] + nums[2]

        if res == target:
        	return target

        for i in xrange(len(nums)):
        	l, r = i + 1, len(nums) - 1
        	while l < r:
        		t = nums[i] + nums[l] + nums[r]
        		if t == target:
        			return target

        		elif t > target:
        			r -= 1
        		else:
        			l += 1
        		if abs(t - target) < abs(res - target):
        			res = t
        return res
