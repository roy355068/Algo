class Solution(object):
	def countPrimes(self, n):
		count = 0
		prime = [False for _ in xrange(n)]
		for i in xrange(2, n):
			if not prime[i]:
				count += 1
				j = 2
				while i * j < n:
					prime[i * j] = True
					j += 1
		return count