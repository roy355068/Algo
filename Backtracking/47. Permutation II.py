class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.p(res, [], nums, [False for _ in xrange(len(nums))], len(nums))
        return res

    def p(self, res, temp, nums, used, length):
    	if len(temp) == length:
    		res.append(temp[:])
    		return
    	for i in xrange(len(nums)):
    		if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
    			continue
    		temp.append(nums[i])
    		used[i] = True
    		self.p(res, temp, nums, used, length)
    		used[i] = False
    		temp.pop()

