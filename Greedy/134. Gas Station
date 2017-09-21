class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if not gas:
        	return -1
        cand, totalNeeded, tank = 0, 0, 0
        for i in xrange(len(gas)):
        	tank += gas[i] - cost[i]
        	if tank < 0:
        		totalNeeded += tank
        		cand = i + 1
        		tank = 0
        return cand if totalNeeded + tank >= 0 else -1