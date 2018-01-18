import random
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """
        self.nums = nums
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        res = -1
        count = 1
        for i in xrange(len(self.nums)):
            if self.nums[i] != target:
                continue
            else:
                # Key!
                # Use reservoir sampling, pick and replace with each sample with 
                # probability of 1 / count
                if random.randrange(count) == 0:
                    res = i
                count += 1
        return res




# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)