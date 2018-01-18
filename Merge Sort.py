class Solution(object):

    def sort(self, nums):
        print nums
        self.mergeSort(nums, 0, len(nums) - 1)
        print nums
    def mergeSort(self, nums, l, r):
        if l < r:
            mid = l + (r - l) / 2
            self.mergeSort(nums, l, mid)
            self.mergeSort(nums, mid + 1, r)
            self.merge(nums, l, mid, r)

    def merge(self, nums, l, m, r):
        lenLeft = m - l + 1
        lenRight = r - m
        left = nums[l : m+1]
        right = nums[m+1 : r+1]
        i, j, k = 0, 0, l

        while i < lenLeft and j < lenRight:
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < lenLeft:
            nums[k] = left[i]
            i += 1
            k += 1
        while j < lenRight:
            nums[k] = right[j]
            j += 1
            k += 1

x = Solution()
x.sort([12, 11, 13, 5, 6, 7])
# x.mergeSort([12, 11, 13, 5, 6, 7], 0, 5)
