class Solution(object):
	def getPermutation(self, n, k):
		"""
		idxs = [0, 1, 2, 3]
		nums = [1, 2, 6, 24]
		cand = [1, 2, 3, 4]
			[1,2,3] =>
			1 + [2, 3] 2
			2 + [1, 3] 2
			3 + [1, 2] 2
			
			k = 5 : "312"

			[1,2,3,4] =>
			1 + [2, 3, 4] 6

			1 2 3 4
			1 2 4 3
			1 3 2 4
			1 3 4 2
			1 4 2 3
			1 4 3 2

			2 + [1, 3, 4] 6
			3 + [1, 2, 4] 6
			4 + [1, 2, 3] 6
		"""
		nums = [1 for _ in xrange(1, 10)]
		cand = [i for i in xrange(1, 10)]

		for i in xrange(len(nums)):
			for j in xrange(1, i + 2):
				nums[i] *= j

		# because k is 1-indexed number, we can make it 0-indexed by minus 1
		k -= 1

		# start examine the number by the factorial of n - 1 digits
		start = n - 2
		res = []

		# do iteration until -1
		# which means need to use every digits in cand
		for i in xrange(start, -2, -1):
			num = nums[i]
			res.append(cand[k // num])
			cand.remove(cand[k // num])
			k %= num
		return "".join(map(str, res))

