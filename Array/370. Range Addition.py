class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        res = [0] * length
        for u in updates:
            res[u[0]] += u[2]
            if u[1] < len(res) - 1:
                res[u[1] + 1] += -u[2]

        for i in xrange(1, len(res)):
            res[i] += res[i - 1]
        return res
