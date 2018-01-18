class Solution(object):
    def findPeakElement(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) / 2
            if mid > 0 and nums[mid - 1] > nums[mid]:
                r = mid - 1
            else:
                # the normal binary search would bias the mid pointer
                # to the left, so that we don't need to check if the
                # mid is  < len(nums) - 1 and can add 1 to it
                # and won't get a error
                if nums[mid] > nums[mid + 1]:
                    return mid
                l = mid + 1
        return l
