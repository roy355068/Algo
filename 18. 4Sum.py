# Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

# Note: The solution set must not contain duplicate quadruplets.

# For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.

# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.helper(sorted(nums), target, res, [], 4)
        return res

    def helper(self, nums, target, res, temp, k):
    	if k < 2 or len(nums) < k or target < nums[0] * k or target > nums[-1] * k:
    		return

    	if k == 2:
    		l, r = 0, len(nums) - 1
    		while l < r:
    			t = nums[l] + nums[r]
    			if t == target:
    				if r < len(nums) - 1 and nums[r] == nums[r + 1] and nums[l] == nums[l - 1]:
    					l += 1
    					r -= 1
    					continue
    				res.append(temp + [nums[l], nums[r]])
    				l += 1
    				r -= 1
    			elif t < target:
    				l += 1
    			else:
    				r -= 1

    	else:
    		for i in xrange(len(nums)):
    			if i == 0 or nums[i] != nums[i - 1]:
    				self.helper(nums[i+1 : ], target - nums[i], res, temp + [nums[i]], k - 1)

