# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Find the minimum element.

# You may assume no duplicate exists in the array.


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        mid = l + (r - l) / 2
        while l <= r:
            mid = l + (r - l) / 2
            if mid > 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]

            # Notice that mid is calculated to be biased to left,
            # So have to check if nums[mid] == nums[l] !!!!
            if nums[mid] >= nums[l] and nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[mid]