class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask, maxXOR = 0, 0
        # Start from the leftmost bit
        for i in xrange(31, -1, -1):
        	# Use mask to extract the status of current bit and the bits left to current
        	mask |= (1 << i)
        	hashSet = set()
        	for num in nums:
        		hashSet.add(num & mask)

        	# a ^ b = c , and we can use the property of XOR
        	# => a ^ c = b and b ^ c = a
        	# so if we can find the element (pre) in the set such that
        	# pre ^ max = something in the set
        	# Then we can say that pre ^ something in the set = max!
        	tempMax = maxXOR | (1 << i)
        	for pre in hashSet:
        		if pre ^ tempMax in hashSet:
        			maxXOR = tempMax
        			break
        return maxXOR
