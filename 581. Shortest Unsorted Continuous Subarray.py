# Given an integer array, you need to find one continuous subarray that 
# if you only sort this subarray in ascending order, then the whole array 
# will be sorted in ascending order, too.

# You need to find the shortest such subarray and output its length.

# Example 1:
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array 
# sorted in ascending order.

# Note:
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=.

class Solution(object):
	def findUnsortedSubarray(self, nums):

		# Solution 1
		# The idea is comparing the sorted and unsorted array and find the leftmost and rightmost
		# index that the order started distorted
		temp = nums[:]
		temp.sort()
		l, r = 0, len(nums) - 1
		for i in xrange(len(nums)):
			if nums[i] != temp[i]:
				l = i
				break
		if i == len(nums) - 1:
			return 0
		for j in xrange(len(nums) - 1, -1, -1):
			if nums[j] != temp[j]:
				r = j
				break
		return r - (l - 1)

		# Solution 2 (Using stack, LC's answer)
		# use stacks to keep tracking the indices that follow the ascending order from the start,
		# or descending order from the end,
		# if there's an element out of order, we can pop the stack and find out what correct index
		# the number should have in the original array to make it "ordered"
		# and use the leftmost and rightmost pointers to calculate the length of subarrays that
		# needed to be sorted
	def stack(self, nums):
		l, r = len(nums) - 1, 0
		# stack is tracking the indices that follow the order
		stack = []
		for i in xrange(len(nums)):
			while stack and nums[stack[-1]] > nums[i]:
				l = min(l, stack.pop())
			stack.append(i)
		stack = []
		for j in xrange(len(nums) - 1, -1, -1):
			while stack and nums[stack[-1]] < nums[j]:
				r = max(r, stack.pop())
			stack.append(j)
		return r - (l - 1) if r - l > 0 else 0







