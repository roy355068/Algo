class Solution(object):
    # Paint all houses such that no adjacent houses have the same color
    # costs is a n * 3 matrix to represent n houses and the corresponding
    # cost to paint each house with different colors
    def minCost(self, costs):
        if not costs:
            return 0

        # use two dp arrays to store the prev work and avoid interfere with
        # the global minimum result
        prev = [val for val in costs[0]]
        colorNum = len(costs[0])
        for i in xrange(1, len(costs)):
            curr = [0 for _ in xrange(colorNum)]

            # j : index in current row
            for j in xrange(colorNum):
                prevMinCost = float('inf')
                # k : index in previous row
                for k in xrange(colorNum):
                    if j != k:
                        # minimal number in the previous row that
                        # is not the same color with the current house
                        prevMinCost = min(prevMinCost, prev[k])

                curr[j] = prevMinCost + costs[i][j]
                
            prev = curr
        return min(prev)
