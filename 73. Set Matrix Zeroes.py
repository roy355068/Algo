
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.


class Solution(object):
    def setZeroes(self, m):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        # Solution 1: Used O(rows + cols) space complexity
        # rows, cols = [], []
        # for i in xrange(len(m)):
        #     for j in xrange(len(m[0])):
        #         if m[i][j] == 0:
        #             if i not in rows:
        #                 rows.append(i)
        #             if j not in cols:
        #                 cols.append(j)
        # for i in xrange(len(m)):
        #     for j in xrange(len(m[0])):
        #         if m[i][j] == 0:
        #             continue
        #         else:
        #             if i in rows or j in cols:
        #                 m[i][j] = 0

        # Solution 2: Followed up, Used O(1) constant space
        # idea is store the info at the first element of each rows and cols, but the 
        # first col and first row would both use the matrix[0][0], which would interfere
        # the true result, so I can use an additional variable to stroe the info for col 0
        # The result of col0 is depends on the status of boolean value of col0, so that
        # we could avoid interefering the first rows
        colzero, rows, cols = False, len(m), len(m[0])
        for i in xrange(rows):
            if m[i][0] == 0:
                colzero = True
            for j in xrange(1, cols):
                
                if m[i][j] == 0:
                    m[i][0] = 0
                    m[0][j] = 0

        for i in xrange(rows - 1, -1, -1):
            for j in xrange(cols - 1, 0, -1):
                if m[i][0] == 0 or m[0][j] == 0:
                    m[i][j] = 0
            if colzero:
                m[i][0] = 0