class Solution(object):
    # in the test of hackerrank, the "weight" and "value" are the same
    # and the only constraint is the total weight "k"
    # a person can pick one item for multiple times

    # First thought, using 2d dp array to store the intermediate results
    # O(r * c) for time and space complexity
    def unboundedKnapsack(k, nums):
        nums = sorted(list(set(nums)))
        dp = [[0 for _ in xrange(k + 1)] for _ in xrange(len(nums))]

        for i in xrange(len(dp)):
            for j in xrange(len(dp[0])):
                currWt = j
                itemWt = nums[i]
                if itemWt > currWt:
                    dp[i][j] = dp[i - 1][j] if i > 0 else 0
                else:
                    if i == 0:
                        # pick the item itself
                        dp[i][j] = itemWt + dp[i][j - itemWt]
                    else:
                        """
                        the current maximum could come from three scenarios
                        1. pick the item once again (if already picked once before)

                        2. pick current item for the first time

                        3. not pick current item but pick the maximal values
                           in the way in the prev row (because picking current
                           item will exceed the constraint)

                        """
                        dp[i][j] = max(itemWt + dp[i][j - itemWt],
                                       itemWt + dp[i - 1][j - itemWt],
                                       dp[i - 1][j])
        return dp[-1][-1]

    # optimized dp solution, using two 1d dp array
    # O(r * c) for time and O(c) for space complexity
    def unboundedKnapsack(k, nums):
        nums = sorted(list(set(nums)))
        prev = [0 for _ in xrange(k + 1)]
        curr = [0 for _ in xrange(k + 1)]

        for i in xrange(len(nums)):
            for j in xrange(k + 1):
                currWt = j
                itemWt = nums[i]
                if itemWt > currWt:
                    curr[j] = prev[j]
                else:
                    curr[j] = max(itemWt + curr[j - itemWt],
                                  itemWt + prev[j - itemWt],
                                  prev[j])
            prev = curr[:]
            curr = [0 for _ in xrange(k + 1)]
        return prev[-1]
        
