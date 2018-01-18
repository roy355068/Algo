from collections import deque

# find the maximum in each "window" and put them into a list
# when iterating through the array, use a deque to store the index encountered so far
class Solution(object):
	def maxSlidingWindow(self, nums, k):
		q, res = deque(), []
		for i in xrange(len(nums)):
			# if there's at least one item in deque, pop the deque from back if
			# the element in deque is samller than current one (since we're looking for maximum)

			# notice that the largest number will always be at the front of the deque
			# since we always start popping from back
			while q and nums[q[-1]] < nums[i]:
				q.pop()

			# check if the deque contains elements that is not suppose to be in this index window
			# if yes, pop left.
			# Notice that the number with smallest indices would be at the front of deque
			while q and i - q[0] >= k:
				q.popleft()
			# append current index to deque
			q.append(i)
			# if the windows saturated, start to append the largest element to the result
			if i >= k - 1:
				res.append(nums[q[0]])
		return res
