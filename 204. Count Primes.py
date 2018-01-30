class Solution(object):
	def countPrimes(self, n):
		count = 0
		# every number is prime by default before we investigate it
		isPrime = [True for _ in xrange(n)]
		for i in xrange(2, n):
			if prime[i]:
				count += 1
				j = 2
				# update the multiple of the prime number to be "not a prime"
				while i * j < n:
					prime[i * j] = False
					j += 1
		return count
