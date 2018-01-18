class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) / 2
            # mid and all of the points left to it are candidates
            if nums[mid] < nums[r]:
                r = mid
            # only elements to the right of mid could be possible
            # to be the smallest number (since mid is already larger)
            # than right pointer
            elif nums[mid] > nums[r]:
                l = mid + 1

            # else if nums[mid] == nums[r]
            # there are two situation
            # 1. the smallest number is in between mid and right
            # think about 1, 1, 1, 1, 0, 1, 1
            # the rotation may happens in the 1s segment

            # 2. the smallest number is on the left of mid
            # eg. 0, 1, 1, 1, 1, 1, 1
            #
            # We don't really have a way to determine which case would be
            # the case, so the safest way to find the smallest element
            # is check each element
            # hence makes the time complexity in the worse case a O(N)
            else:
                r -= 1
        return nums[l]
