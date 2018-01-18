# Find the contiguous subarray within an array (containing at least one number) which has the 
# largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
        	return nums[0]

        # My solution
        new = [0 for _ in xrange(len(nums))]
        new[0] = nums[0] if nums[0] > 0 else 0
        for i in xrange(1, len(nums)):
        	new[i] = new[i - 1] + nums[i] if new[i - 1] + nums[i] > 0 else 0
        return max(nums) if max(nums) < 0 else max(new)

        # Optimized solution : use m to record the "SoFar Max"
        new = [0 for _ in xrange(len(nums))]
        new[0], m = nums[0], nums[0]
        for i in xrange(1, len(nums)):
            new[i] = nums[i] + (new[i - 1] if new[i - 1] > 0 else 0)
            m = max(m, new[i])
        return m