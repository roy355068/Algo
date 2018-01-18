# Given a non-empty array of integers, return the k most frequent elements.

# For example,
# Given [1,1,1,2,2,3] and k = 2, return [1,2].

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Bucket sort : use an array to store frequencies : numbers
        # Then collect data from the rear (higher frequencies) of the array
        
        # dictionary store numbers : frequencies
        dic = {}
        for num in nums:
        	dic[num] = dic.get(num, 0) + 1
        
        buckets = [[] for _ in xrange(len(nums) + 1)]
        # store frequencies : numbers in buckets
        for key, val in dic.items():
        	buckets[val].append(key)

        res = []
        for i in xrange(len(buckets) - 1, -1, -1):
        	if buckets[i]:
        		for element in buckets[i]:
        			res.append(element)
        		k -= len(buckets[i])
        		if k <= 0:
        			break
        return res

        # Use a array to store the numbers : frequencies, then sort it!
        dic = {}
        for num in nums:
        	dic[num] = dic.get(num, 0) + 1
        l = []
        for key, val in dic.items():
        	l.append([key, val])
        l.sort(reverse = True, key = lambda x : x[1])
        res = []
        for i in xrange(k):
        	res.append(l[i][0])
        return res


