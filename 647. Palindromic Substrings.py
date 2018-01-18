# Given a string, your task is to count how many palindromic substrings in this string.

# The substrings with different start indexes or end indexes are counted as different substrings 
# even they consist of same characters.

# Example 1:
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Example 2:
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

# Note:
# The input string length won't exceed 1000.

class Solution(object):
	def __init__(self):
        self.count = 0
    def countSubstrings(self, s):
        for i in xrange(len(s)):
            self.isP(s, i, i)
            self.isP(s, i, i + 1)
        return self.count

    def isP(self, s, l, r):
        while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
            self.count += 1
            l -= 1
            r += 1