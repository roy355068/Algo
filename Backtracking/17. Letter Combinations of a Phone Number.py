# Given a digit string, return all possible letter combinations that the number could represent.
# A mapping of digit to letters (just like on the telephone buttons) is given below.

# Input:Digit string "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

class Solution(object):
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		if not digits:
			return []
		mapping = {
			'2': 'abc',
			'3': 'def',
			'4': 'ghi',
			'5': 'jkl',
			'6': 'mno',
			'7': 'pqrs',
			'8': 'tuv',
			'9': 'wxyz'
		}
		res = [""]
		for i in xrange(len(digits)):
			chars = mapping[digits[i]]
			while len(res[0]) == i:
				temp = res.pop(0)
				for char in chars:
					res.append(temp + char)
		return res