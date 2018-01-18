class Solution(object):
    def minSubArrayLen(self, s, nums):

        # Brute Force. O(N ^ 2) time complexity
        res = float('inf')
        if nums:
            for i in xrange(len(nums)):
                tempSum = nums[i]
                if tempSum >= s:
                    return 1
                for j in xrange(i + 1, len(nums)):
                    tempSum += nums[j]
                    if tempSum >= s:
                        res = min(res, j - i + 1)
                        break
        return res if res != float('inf') else 0

    # Two Pointers Solution, move tail pointer first to get temporarily
    # get the local maximal length, then use another head pointer
    # to shrink the window to derive the minimal length of subarray
    # that fulfill the requirement of the question
    # O(N) time complexity
    def minSubArrayLen(self, s, nums):
        res = float('inf')
        if nums:
            i, j, tempSum = 0, 0, 0
            while j < len(nums):
                tempSum += nums[j]
                # while tempSum is greater or equal to s
                # shrink the window to find the possible minial lenght of
                # subarray since it would be possible that only little
                # amount of elements on the right side could fulfill the requirement
                while tempSum >= s and i < len(nums):
                    res = min(res, j - i + 1)
                    tempSum -= nums[i]
                    i += 1
                j += 1
        return res if res != float('inf') else 0

    # Binary Search solution. Since the array is not sorted, but the running sum
    # will be sorted (monotonically inceasing) due to the fact that there are
    # all positive number in the array, we can then use binary search
    # in the new "sorted" array to find the possible min length that sums up to s
    def minSubArrayLen(self, s, nums):
        res = float('inf')
        if nums:
            sortedNums = [0 for _ in xrange(len(nums))]
            sortedNums[0] = nums[0]
            for i in xrange(1, len(nums)):
                sortedNums[i] += nums[i - 1]
            # Because the elements in sortedNums is the running sum of the nums array
            # we can subtract any to element in sortedNums to derive the sum of nums element
            # between those two indices
            for i in xrange(len(sortedNums)):
                curr = sortedNums[i]
                l, r = i + 1, len(sortedNums) - 1
                while l < r:
                    mid = l + (r - l) / 2
                    if nums[mid] - nums[curr] < s:
                        l = mid + 1
                    else:
                        r = mid
                res = min(res, r - l + 1)
        return res if res != float('inf') else 0
