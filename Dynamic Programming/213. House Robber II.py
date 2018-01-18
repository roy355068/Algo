class Solution(object):
    # since the head and tail of the list is linked
    # we could use a helper function to decide
    # will rob the first house or not rob it to have the max value
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums, 0, len(nums) - 2),
                    self.helper(nums, 1, len(nums) - 1))

    def robRange(self, nums, l, r):
        prevNo, prevYes = 0, 0
        for i in xrange(l, r + 1):
            currNo = max(prevNo, prevYes)
            currYes = prevNo + nums[i]
            prevNo, prevYes = currNo, currYes
        return max(prevNo, prevYes)
