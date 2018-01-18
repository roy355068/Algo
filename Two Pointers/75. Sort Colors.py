class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        l, i, r = 0, 0, len(nums)
        while i <= r:
        	""" 
        	if curr index is 0, and l is not 0 swap it with the number on l index
        	increment l to keep track the tail of 0
        	"""
        	if nums[i] == 0:
        		if nums[l] != 0:
        			nums[l], nums[i] = nums[i], nums[l]
        		l += 1
        	# same here, swap curr with right index
        	# but i needs to stay in current position to be examined
        	# if it's a 1 or 0 and do the swapping
        	elif nums[i] == 2:
        		if nums[r] != 2:
        			nums[r], nums[i] = nums[i], nums[r]
        		r -= 1
        		i -= 1
        	i += 1