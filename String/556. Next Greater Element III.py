# Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which 
# has exactly the same digits existing in the integer n and is greater in value than n. 
# If no such positive 32-bit integer exists, you need to return -1.

# Example 1:
# Input: 12
# Output: 21

# Example 2:
# Input: 21
# Output: -1

# Similar Question : No. 31 in Arrays

class Solution(object):
	def nextGreaterElementConstantSpace(self, n):
		num = list(str(n))
		i = len(num) - 2
		while i >= 0 and int(num[i]) >= int(num[i + 1]):
			i -= 1
		if i < 0:
			return -1
		j = len(num) - 1
		while j >= 0 and int(num[j]) <= int(num[i]):
			j -= 1
		num[i], num[j] = num[j], num[i]
		l, r = i + 1, len(num) - 1
		while l < r:
			num[l], num[r] = num[r], num[l]
			l += 1
			r -= 1
		res = int("".join(num))
		return res if res < (2 ** 31) - 1 else -1

	def nextGreaterElement(self, n):
		s = str(n)
		stack, pos, found, pivotVal = [], 0, False, 0
		for i in xrange(len(s) - 1, -1, -1):
			stack.append(int(s[i]))
			if int(s[i]) < max(stack):
				pos = i
				pivotVal = int(s[pos])
				found = True
				break
		if not found:
			return -1
		stack.sort()
		nextLargest = 0
		for j in stack:
			if j > pivotVal:
				nextLargest = j
				stack.remove(j)
				break
		temp = int(s[:pos] + str(nextLargest) + "".join(map(str, stack)))
		return temp if temp < (2 ** 31) - 1 else -1
