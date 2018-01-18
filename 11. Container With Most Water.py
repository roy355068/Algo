class Solution(object):
    def maxArea(self, height):
        if not height:
            return 0
        res, l, r = 0, 0, len(height) - 1
        # no need to check the situation when l == r, because l == r
        # would result in 0 value
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            # if height[l] is smaller or equal to height[r]
            # it might be helpful if move l to right since the
            # volume is controlled by the side that has the lower height
            # vice versa
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res
