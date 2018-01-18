class Solution(object):
	def lengthOfLIS(self, nums):
		n = len(nums)
		if n < 2:
			return n
		last = [0 for _ in xrange(n)]
		m = 0
		for i in xrange(n):
			l, r = 0, m
			while l < r:
				mid = l + (r - l) / 2
				if last[mid] < nums[i]:
					l = mid + 1
				else:
					r = mid
			last[l] = nums[i]
			if l == m:
				m += 1
		return m