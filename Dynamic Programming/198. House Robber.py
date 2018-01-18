# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses were broken into
# on the same night.

# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.


# The idea is use another array (total, if don't want to modify the original array) to
# take record of the robbing process
# each element of total keep tracking the maximum amount the robber can get in this current
# postion
# the the max of total[i - 1] and nums[i] + total[i - 2] to see if he can get a higher amount
# of money by skipping the previous one house to avoid the alarm, or by robbing the previous
# one house
class Solution(object):

    # O(N) for both time and space complexity
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0
        elif len(nums) <= 2:
        	return max(nums)
        nums[1] = max(nums[0], nums[1])

        for i in xrange(2, len(nums)):
            # update current element by
            # taking the max of robbing previous house
            # or not robbing previous house
        	nums[i] = max(nums[i - 1], nums[i] + nums[i - 2])
        return nums[-1]

    def robWithArg(self, nums, w):
        if not nums:
            return 0
        tempMax = max(nums[:w])
        for i in xrange(w):
            nums[i] = tempMax

        for i in xrange(w, len(nums)):
            currYes = nums[i - w] + nums[i]
            currNo = nums[i - w + 1]
            for j in xrange(2, w - 1):
                currNo = max(currNo, nums[i - w + j])
            nums[i] = max(currYes, currNo)
        return nums[-1]
            
    # optimized solution : O(N) time and O(1) space complexity
    def rob(self, nums):
        prevNo = 0
        prevYes = 0
        for n in nums:
            currYes = prevNo + n
            currNo = max(prevNo, prevYes)
            prevYes = currYes
            prevNo = currNo
        return max(prevYes, prevNo)
