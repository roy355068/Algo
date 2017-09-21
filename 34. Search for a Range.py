# Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        if not nums:
        	return res
        l, r = 0, len(nums) - 1
        while l < r:
        	mid = l + (r - l) / 2
        	if nums[mid] < target:
        		l = mid + 1
        	else:
        		r = mid
        if nums[l] != target:
        	return res
        res[0] = l
        l, r = 0, len(nums) - 1
        while l < r:
        	mid = (l + (r - l) / 2) + 1
        	if nums[mid] > target:
        		r = mid - 1
        	else:
        		l = mid
        res[1] = r
        return res





