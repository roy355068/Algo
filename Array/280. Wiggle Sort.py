class Solution(object):
    def wiggleSort(self, nums):
        for i in xrange(1, len(nums)):
            if (i % 2 == 1) == (nums[i - 1] > nums[i]):
                nums[i - 1], nums[i] = nums[i], nums[i - 1]

    # Alternative way, sort the array then swap the element pairwise
    # starting at second 2
    def wiggleSort(self, nums):
        nums.sort()
        for i in xrange(1, len(nums) - 1, 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
