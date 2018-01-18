class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.comb(res, [], n, k, 1)
        return res
    def comb(self, res, temp, n, k, start):
    	if k == 0:
    		res.append(temp[:])
    		return
    	for i in xrange(start, n - k + 2):
    		temp.append(i)
    		self.comb(res, temp, n, k - 1, i + 1)
    		temp.pop()