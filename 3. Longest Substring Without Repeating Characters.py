class Solution(object):
	def lengthOfLongestSubstring(self, s):
		use l, r to indicate start and running pointer
		maxLen, dic, l, r = 0, {}, 0, 0
		for r in xrange(len(s)):
			if s[r] in dic:
				# if there's a repeated char in previous substring,
				# move the starting point to next index of that repeated char.
				
				# the repeated chars may have lower index than the current starting index
				# in that case, the value won't be available, so l = max(l, dic[s[r]] + 1)
				l = max(l, dic[s[r]] + 1)
			dic[s[r]] = r
			maxLen = max(maxLen, r - l + 1)
		return maxLen


