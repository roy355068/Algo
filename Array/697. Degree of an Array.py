from collections import *
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        mostCommon = count.most_common(1)
        degree = count[mostCommon[0][0]]
        mostCommon = set()

        for k, v in dict(count).items():
            if v == degree:
                mostCommon.add(k)

        dic = defaultdict(list)
        res = len(nums)

        for i, v in enumerate(nums):
            if v in mostCommon:
                dic[v].append(i)
                if len(dic[v]) == degree:
                    res = min(res, dic[v][-1] - dic[v][0] + 1)
        return res

    def findShortestSubArray(self, nums):
        dic = {}
        # use a list to store the status of each number in nums
        for i, v in enumerate(nums):
            if v not in dic:
                dic[v] = [1, i, i]
            else:
                dic[v][0] += 1
                dic[v][2] = i

        degree, res = float('-inf'), float('inf')
        for vals in dic.values():
            currDist = vals[2] - vals[1] + 1
            currDegree = vals[0]
            if currDegree > degree:
                degree = currDegree
                res = currDist
            elif currDegree == degree:
                res = min(res, currDist)
        return res
