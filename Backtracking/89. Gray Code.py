class Solution(object):
	
	# If disregard the leftmost digit, the pattern observed is that the second half
	# if symmetric to the first half
	#
	def grayCode(self, n):
		res = [0]
		for i in xrange(n):
			for j in xrange(len(res) - 1, -1, -1):
				res.append(res[j] | 1 << i)
		return res