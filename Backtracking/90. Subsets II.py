class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.subset(res, [], nums, 0)
        return res
    def subset(self, res, temp, nums, start):
        res.append(temp[:])
        for i in xrange(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            temp.append(nums[i])
            self.subset(res, temp, nums, i + 1)
            temp.pop()
            