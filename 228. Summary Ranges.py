class Solution(object):
    def summaryRanges(self, nums):
        res = []
        i = 0
        while i < len(nums):
            head = nums[i]
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1
            tail = nums[i]
            if head != tail:
                res.append(str(head) + "->" + str(tail))
            else:
                res.append(str(head))
        return res
