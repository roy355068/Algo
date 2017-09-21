# Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Note:
# You may assume the interval's end point is always bigger than its start point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
# Example 1:
# Input: [ [1,2], [2,3], [3,4], [1,3] ]

# Output: 1

# Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
# Example 2:
# Input: [ [1,2], [1,2], [1,2] ]

# Output: 2

# Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
# Example 3:
# Input: [ [1,2], [2,3] ]

# Output: 0

# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# The idea is that, if we sort the array with data's endpoints, we can tell if the data point
# (interval) is good or not by looking at if the starting points of following intervals fall before 
# the current end points

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
    	"""
        :type intervals: List[Interval]
        :rtype: int
        """
    	if not intervals:
    		return 0
    	intervals.sort(key = lambda x : x.end)
    	end = intervals[0].end
    	# goodCount is the number of elements that don't need to be removed
    	goodCount = 1
    	for i in xrange(1, len(intervals)):
    		if intervals[i].start >= end:
    			goodCount += 1
    			end = intervals[i].end
    	return len(intervals) - goodCount


