
class Solution(object):
    def threeSumSmaller(self, nums, target):
        nums.sort()
        res = 0
        for i in xrange(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                temp = nums[i] + nums[l] + nums[r]
                if temp < target:
                    # cuz everything in the range of (left + 1, right)
                    # would also smaller than target, so count them at once
                    res += r - l
                    l += 1
                else:
                    r -= 1
        return res
