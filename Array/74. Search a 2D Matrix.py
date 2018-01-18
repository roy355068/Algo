class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        l, r = 0, len(matrix) - 1
        while l < r:
            mid = 1 + l + (r - l) / 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                l = mid
        row = l
        print row
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = l + (r - l) / 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False


    def searchMatrix(self, matrix, target):
        # transform an m * n matrix into sorted array
        # matrix[x][y] = array[x * n + y]

        # transform a sorted array into m * n matrix
        # array[x] = matrix[x / n][x % n]
        m, n = len(matrix), len(matrix[0])
        # r is the element at the down-right corner
        l, r = 0, m * n - 1
        while l < r:
            mid = l + (r - l) / 2
            if matrix[mid / n][mid % n] < target:
                l = mid + 1
            else:
                r = mid
        return matrix[r / n][r % n] == target
