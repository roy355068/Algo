class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
        	n = -n
        	x = 1/x
        if n == 0:
        	return 1
        elif n == 1:
        	return x
        elif n == 2:
        	return x * x
        return self.myPow(x * x, n / 2) if n % 2 == 0 else x * self.myPow(x * x, n / 2)