# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True

# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.

# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
        	return True
        l, r = 0, len(s) - 1
        while l <= r:
        	# Due to the restriction of "at most one modification", after encountering an error
        	# use recursion to examine the string from l + 1 to r, and l to r - 1, to see if 
        	# the skipping could generate an palindrome or not.
        	if s[l] != s[r]:
        		return self.isP(s, l + 1, r) or self.isP(s, l, r - 1)
        	l += 1
        	r -= 1
        return True
    def isP(self, s, l, r):
    	while l <= r:
    		if s[l] != s[r]:
    			return False
    		l += 1
    		r -= 1
    	return True