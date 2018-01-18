# You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

# Define a pair (u,v) which consists of one element from the first array and one element 
# from the second array.

# Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

from heapq import *



class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2 or k <= 0:
        	return []
        h = []
        # can put tuple as element into heap, the heap would take the first argument and 
        # use its value as sorting key
        for num in nums1:
        	heappush(h, (num + nums2[0] , num, nums2[0], 0))

        res = []
        for i in xrange(k):
        	if h:
        		curr = heappop(h)
        		res.append([curr[1], curr[2]])
        		nums2Index = curr[3]
        		if nums2Index == len(nums2) - 1:
        			continue
        		else:
        			heappush(h, (curr[1] + nums2[nums2Index + 1], curr[1], nums2[nums2Index + 1], nums2Index + 1))
        return res