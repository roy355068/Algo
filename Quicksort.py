class Solution(object):

    def QuickSort(self, nums):
        self.QuickSortHelper(nums, 0, len(nums) - 1)
        print nums

    def QuickSortHelper(self, nums, low, high):
        # guard check that check the invariants of the function (low must
        # smaller than high)
        if low < high:
            pivot = self.partition(nums, low, high)
            self.QuickSortHelper(nums, low, pivot - 1)
            self.QuickSortHelper(nums, pivot + 1, high)

    def partition(self, nums, low, high):
        pivot = nums[high] # take the last element as pivot
        i = low - 1
        for j in xrange(low, high):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[high] = nums[high], nums[i + 1]
        return i + 1

x = Solution()
x.QuickSort([10, 80, 30, 90, 40, 50, 70])
