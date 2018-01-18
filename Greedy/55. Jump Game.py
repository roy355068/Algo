# Given an array of non-negative integers, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Determine if you are able to reach the last index.

# For example:
# A = [2,3,1,1,4], return true.

# A = [3,2,1,0,4], return false.


# Idea is that use a maximumReach variable to track the max range of the array can reach
# if i > m, indicated that i is not reachable by previous element and jumping
# so end the program earlier and return False, else if maximumReach >= the index of
# last element, meaning that the last element is reachable, return True
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # O(N ^ 2) time, O(N) space complexity
        if not nums or len(nums) == 1:
            return True
        # jump array is a dp array that used to check if the index is reachable
        jump = [False for _ in xrange(len(nums))]
        jump[0] = True
        for i in xrange(len(nums)):
            step = nums[i]
            j = i + 1
            # jump[i] == True means that this index is reachable based
            # on the jump steps before it
            if jump[i] == True:
                # update all indices that is reachable from current stand point
                while j <= len(nums) - 1 and j < i + step + 1:
                    jump[j] = True
                    j += 1
        return jump[-1]

        # Optimized, O(N) time, O(1) space complexity
        i, reachable = 0, 0
        # if i exceeds reachable, meaning that current index is never going
        # to be reachable by jumping from previous indices
        # hence stop the loop earlier
        while i < len(nums) and i <= reachable:
            reachable = max(reachable, i + nums[i])
            i += 1
        return i == len(nums)
