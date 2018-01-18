# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example:
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example:
# Input: "cbbd"
# Output: "bb"

class Solution(object):
	def __init__(self):
		self.max = 0
		self.res = ""
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i in xrange(len(s)):
        	self.isP(s, i, i, 0)
        	self.isP(s, i, i + 1, 0)
        return self.res
    def isP(self, s, l, r, t):
    	while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
    		t = (r + 1) - l
    		if t > self.max:
    			self.max = t
    			self.res = s[l : r + 1]
    		l -= 1
    		r += 1

        