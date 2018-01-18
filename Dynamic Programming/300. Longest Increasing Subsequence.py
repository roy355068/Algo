class Solution(object):
    # O(N ^ 2) time complexity
    # O(N) space complexity for the dp array
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        # Initialize the dp with all 1 because all element by definition
        # is their LIS when only have one number
        dp = [1 for _ in xrange(len(nums))]
        # default res would be one for the same reason
        res = 1
        for i in xrange(len(nums)):
            # maxLen will update when scanning through the subarray
            # before index i
            # only update the value when there's a value that is smaller
            # than current number
            maxLen = 0
            for j in xrange(i):
                if nums[j] < nums[i]:
                    maxLen = max(maxLen, dp[j])
            dp[i] += maxLen
            res = max(res, dp[i])
        return res
