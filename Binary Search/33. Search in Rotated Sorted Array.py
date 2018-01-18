class Solution(object):
	def search(self, nums, target):
		if not nums:
			return -1
		l, r = 0, len(nums) - 1
		while l < r:
			mid = l + (r - l) / 2

			if nums[mid] == target:
				return mid
			# 順向subarray 1, 2, 3, 4, 5, 6
			if nums[l] <= nums[mid]:
				if nums[l] <= target < nums[mid]:
					r = mid - 1
				else:
					l = mid + 1

			# 逆向 (有rotation in subarray)
			# 5, 6, 1, 2, 3, 4
			else:
				if nums[mid] < target <= nums[r]:
					l = mid + 1
				else:
					r = mid - 1
		return l if nums[l] == target else -1
