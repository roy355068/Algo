class Solution(object):
    def containsDuplicate(self, nums):
        # 1st, transform the list into a set and compare the len of them
        # O(N) for both space and time complexity due to
        # converting the list into set and storing the set
        return len(nums) > 0 and len(set(nums)) != len(nums)

        # 2nd, use dictionary to store the index
        # O(N) for both space and time complexity as well
        dic = {}
        for n in nums:
            if n in dic:
                return True
            dic[n] = 1
        return False

        # 3rd, sort the nums array and check if the adjacent num has
        # a same value as current one
        # O(N Log N) time complexity and O(1) space complexity
        nums.sort()
        for i in xrange(1, nums):
            if nums[i - 1] == nums[i]:
                return True
        return False

    def containsNearbyDuplicate(self, nums, k):

        # 1st, use a dictionary to store all indices and check if
        # previous index of the same value is smaller or equal to k
        # O(N) for both time and space complexity
        dic = {}
        for i in xrange(len(nums)):
            prev = dic.get(nums[i], -1)
            if prev != -1 and i - prev[-1] <= k:
                return True
            dic.setdefault(nums[i], []).append(i)
        return False

        # 2nd, optimized 1st solution that I only keep a sliding window with
        # length k
        # Time complexity would be O(N), but space would be O(min (N, K))
        # so that we might be able to save some space if K is smaller than N
        numSet = set()
        for i in xrange(len(nums)):
            if nums[i] in numSet:
                return True
            numSet.add(nums[i])
            if len(numSet) > k:
                numSet.remove(nums[i - k])
        return False
