class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.subset(res, [], nums, 0)
        return res
    
    def subset(self, res, temp, nums, start):
        res.append(temp[:])
        for i in xrange(start, len(nums)):
            temp.append(nums[i])
            self.subset(res, temp, nums, i + 1)
            temp.pop()