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
            l, r = 0, len(nums) - 1
            while l < r:
                # if nums[l] < nums[r] means there's no rotation in the subarray (ascending order)
                # so directly return the first element in the subarray
                if nums[l] < nums[r]:
                    return nums[l]
                # else, the array is distorted so the minimum value won't be
                # nums[l] but some other value at the right part of the remaining
                # array
                else:
                    mid = l + (r - l) / 2
                    # if nums[mid] >= nums[l], means the rotation happened in the second segment
                    if nums[mid] >= nums[l]:
                        l = mid + 1
                    # else, means the rotation happened in the first segment
                    # r need to include mid because if nums[mid] < nums[l],
                    # mid is still possible to be the index of the smallest number
                    else:
                        r = mid
            return nums[l]

    # Another thought (but couldn't early terminate the loop)
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) / 2
            # if l > mid, telling us that the subarray is rotated
            # and the smallest element would be mid or to the left of mid
            if nums[l] > nums[mid]:
                r = mid
            # else, meaning the subarray between l and mid is sorted
            # but still need to compare values at mid and right
            # to see which side of the candidate should be
            else:
                # the whole subarray from l to r is sorted,
                # the min val would at the left of mid
                if nums[mid] < nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return nums[l]
