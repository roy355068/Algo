# Implement next permutation, which rearranges numbers into the lexicographically
# next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order
# (ie, sorted in ascending order).

# The replacement must be in-place, do not allocate extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are
# in the right-hand column.
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
		# Start from the beginning
        i = 0
        pivot = 0
		# Find the point (i) that has the trend to increase its value
		# Then find the most suitable pivot, which would be larger
		# then nums[i] but should be the next smallest number
        for j in xrange(len(nums)):
            if j > 0 and nums[j - 1] < nums[j]:
                i = j - 1
                pivot = j
            if pivot != 0 and nums[i] < nums[j] < nums[pivot]:
                pivot = j
        if i == 0 and pivot == 0:
            l, r = 0, len(nums) - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        else:
            nums[i], nums[pivot] = nums[pivot], nums[i]
            print i
            for l in xrange(i + 1, len(nums)):
                for r in xrange(l + 1, len(nums)):
                    if nums[l] > nums[r]:
                        nums[l], nums[r] = nums[r], nums[l]

	def nextPermutation(self, nums):

		i = len(nums) - 2
		while i >= 0 and nums[i + 1] <= nums[i]:
			i -= 1
		if i >= 0:
			j = len(nums) - 1
			while j >= 0 and nums[j] <= nums[i]:
				j -= 1
			nums[i], nums[j] = nums[j], nums[i]
		self.reverse(nums, i + 1)

	def reverse(self, nums, start):
		i, j = start, len(nums) - 1
		while i < j:
			nums[i], nums[j] = nums[j], nums[i]
