# We define a harmonious array is an array where the difference between its maximum value 
# and its minimum value is exactly 1.

# Now, given an integer array, you need to find the length of its longest harmonious subsequence
#  among all its possible subsequences.

class Solution(object):
	def findLHS(self, nums):
		"""
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
        	return 0
        dic = {}
        for i in nums:
        	dic[i] = dic.get(i, 0) + 1
        keys = sorted(dic.keys())
        m = 0
        for i in xrange(len(keys) - 1):
        	if keys[i + 1] - keys[i] == 1:
        		temp = dic[keys[i + 1]] + dic[keys[i]]
        		if temp > m:
        			m = temp
        return m