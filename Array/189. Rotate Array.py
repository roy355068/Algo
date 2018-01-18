class Solution(object):
    # O(N) time, O(1) Space
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums) - k - 1)
        self.reverse(nums, len(nums) - k, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)

    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
            l += 1

    # O(N) time, O(N) Space, additional array space
    def rotate(self, nums, k):
        res = [0 for _ in xrange(len(nums))]
        for i in xrange(len(nums)):
            res[(i + k) % len(nums)] = nums[i]
        for i in xrange(len(nums)):
            nums[i] = res[i]
