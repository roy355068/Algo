class Solution(object):

	# Key idea is that the volumn is controlled by the height of the 
	# lower side of the box
	def maxArea(self, height):
		res, l, r = float('-inf'), 0, len(height) - 1
		while l <= r:
			res = max(res, (r - l) * min(height[l], height[r]))
			# if h[l] is smaller than h[r], it's not possibe finding a right point of 
			# the box that has a larger volumn than current box
			# cuz if the side between l and r has a higher value it still 
			# couldn't increase the vol since the vol is controlled by the lower side
			# if there's a or equal height of right side to left side
			# the decrease of x axis would make it still smaller than current max
			# if it's smaller than left, then the volumn gurantees to be smaller
			# than curr Max
			# So no need to move right pointer, but increment left pointer instead
			# Same logic works for the right pointer!
			if height[l] <= height[r]:
				l += 1
			else:
				r -= 1
		return res