class Solution(object):
    def insert(self, intervals, newInterval):
        i = 0
        while i < len(intervals) and intervals[i].end < newInterval.start:
            i += 1
        while i < len(intervals) and intervals[i].start <= newInterval.end:
            newInterval.start = min(newInterval.start, intervals[i].start)
            newInterval.end = max(newInterval.end, intervals[i].end)
            del intervals[i]
        intervals.insert(i, newInterval)
        return intervals
