class Solution(object):

    # O(N) complexity for both time and space
    def __init__(self):
        self.ans = 0

    def pathSum(self, nums):
        if nums:
            dic = {x / 10 : x % 10 for x in nums}
            self.helper(dic, nums[0] / 10, 0)
        return self.ans

    def helper(self, dic, node, runningSum):
        if node not in dic:
            return
        runningSum += dic[node]
        depth, position = divmod(node, 10)
        right = 10 * (depth + 1) + 2 * position
        left = right - 1
        if right not in dic and left not in dic:
            self.ans += runningSum
        self.helper(dic, left, runningSum)
        self.helper(dic, right, runningSum)
