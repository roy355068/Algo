class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.p(res, [], nums)
        return res
    def p(self, res, temp, nums):
    	if len(temp) == len(nums):
    		res.append(temp[:])
    		return
    	for i in nums:
    		if i in temp:
    			continue
    		temp.append(i)
    		self.p(res, temp, nums)
    		temp.pop()

if __name__ == '__main__':
    s = Solution()
    print s.permute([1,2,3])
    print s.permute([1,2,3,4])