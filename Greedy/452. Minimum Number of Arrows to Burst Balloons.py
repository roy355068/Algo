# There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

# An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

# Example:

# Input:
# [[10,16], [2,8], [1,6], [7,12]]

# Output:
# 2

# Explanation:
# One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).


# The solution is very similar to 435. Non-overlapping intervals
# The way of thinking this problem is, if we sort the array with each end points of the data
# and if we pick the end point (as right as possible) every time when we encounter a data
# , we can be sure that it could burst all ballon that start before this point (since all the 
# ballons are sorted by the end points)

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points:
        	return 0
        points.sort(key = lambda x : x[1])
        count = 1
        endPos = points[0][1]
        for i in xrange(1, len(points)):
        	if points[i][0] > endPos:
        		count += 1
        		endPos = points[i][1]
        return count
