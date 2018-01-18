class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res, temp = [], []
        self.helper(res, temp, s, 0)
        return res


    def helper(self, res, temp, s, start):
    	# if there's already some palindromic string in temp
    	# and the current substring contains the last character (meaning the string is fully
    	# partitioned ) , then it's the valid substring, append it into the result list
    	if len(temp) > 0 and start >= len(s):
    		res.append(temp[:])

    	for i in xrange(start, len(s)):
    		if self.isPa(s, start, i):
	    		if i == start:
	    			temp.append(s[i])
	    		else:
	    			temp.append(s[start : i + 1])
	    		self.helper(res, temp, s, i + 1)
	    		temp.pop()
        
    def isPa(self, s, l, r):
    	while l < r:
    		if s[l] != s[r]:
    			return False
    		l += 1
    		r -= 1
    	return True