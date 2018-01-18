class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.cSum(res, [], candidates, target, 0)
        return res
    
    def cSum(self, res, temp, nums, remain, start):
        if remain < 0:
            return
        elif remain == 0:
            res.append(temp[:])
            return
        else:
            for i in xrange(start, len(nums)):
                temp.append(nums[i])
                # the new start of the next round of recursion is still i because the problem allows 
                # picking the same number for multiple times
                self.cSum(res, temp, nums, remain - nums[i], i)
                temp.pop()
        