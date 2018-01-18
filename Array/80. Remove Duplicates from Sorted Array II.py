class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        # use two pointer i and j
        # i is the last index of the updated array
        # j is a moving pointer scanning the whole array
        i, j = 0, 0
        while i < len(nums) and j < len(nums):
            nums[i] = nums[j]
            # if i is smaller than 2 (== 0 or == 1), the number would
            # be guaranteed to fulfill the requirement of the question

            # other than i < 2, if current ending points is equal to
            # the previous element that is two indices away from current index
            # meaning we already got two copy of a single value, so don't
            # grow the list
            if i == 0 or i == 1 or nums[j] != nums[i - 2]:
                i += 1
            j += 1
        return i

    def removeDuplicates(self, nums):
        # Stephan's version
        i = 0
        for n in nums:
            # same as the previous solution
            if i < 2 or n != nums[i - 2]:
                nums[i] = n
                i += 1
        return i
