# Find the contiguous subarray within an array (containing at least one number)
# which has the largest product.

# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.

class Solution(object):
	def maxProduct(self, nums):
		r, imax, imin = nums[0], nums[0], nums[0]

		for i in xrange(1, len(nums)):
			# if nums[i] < 0, it will makes larger number to smaller number by
			# changing its sign, vice versa
			# So if current number nums[i] < 0, swap imax and imin
			if nums[i] < 0:
				imax, imin = imin, imax

			# The rest of the program is calculate the imax and imin for the possible swapping
			# processes
			# because we need to find the consecutive sequence of array that
			# has maximum product, we need to determine which of the current number or
			# previous product be greater.

			# if current number is greater, then abandon previous max prodcut
			# and do the calculation as if we start at current point
			# same logic for getting min
			imax = max(nums[i], nums[i] * imax)
			imin = min(nums[i], nums[i] * imin)
			r = max(imax, r)

		return r
