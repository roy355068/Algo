# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# You may assume the dictionary does not contain duplicate words.

# For example, given
# s = "leetcode",
# dict = ["leet", "code"].

class Solution(object):
	def wordBreak(self, s, wordDict):
		"""
		dp in this case works as a indicator of the starting indices of each subword that
		can be found in the wordDict

		dp[0] = True because the very first char is a valid starting point of an substring(
		which in this case would be the starting point of the whole string)

		length of dp is len(s) + 1 because by checking the dp[-1] we could tell
		if the dictionary contains the right set of words in order to make the starting index
		cursor to beyond the whole string
		"""
		dp = [False for _ in xrange(len(s) + 1)]
		dp[0] = True
		"""
		i work as the ending points of each substring.
		Due to the fact that the ending index in list slicing is exclusive, we have to
		increase the upper bound of i by 1 to include all chars in the string

		j is the starting points of each substring.
		By checking if the char on jth position is a valid starting point of substring (dp[j])
		and checking if the substring from j to i - 1 in the wordDict,
		we can set the next starting point at i to indicate that we already done
		the searching from j to i - 1.

		Next time the loop would look at the starting point at i and keep doing rest of the work
		again.

		A way to optimize the loops is to count j from i - 1 to 0, instead of counting 0 to i - 1.
		In that way, j doesn't need to go through the substring that had been identified as
		valid.
		"""
		for i in xrange(len(s) + 1):
			for j in xrange(i - 1, -1, -1):
				# if jth to (i-1)th is a valid substring in wordDict
				if dp[j] and s[j : i] in wordDict:
					# set the next starting point
					dp[i] = True
					break
		# See if the wordDict can move the i beyond the length of the string
		return dp[-1]
