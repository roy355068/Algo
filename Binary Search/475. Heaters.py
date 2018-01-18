class Solution(object):
	def findRadius(self, houses, heaters):
		heaters.sort()
		result = float('-inf')

		# check the distance between current house and left/right heaters respectively
		# pick the minimum distance between the heater and house
		# but pick the maximum distance of all data pair since the heater need to cover all houses
		for house in houses:
			idx = self.searchInsert(heaters, house)
			distLeft = house - heaters[idx - 1] if idx >= 1 else float('inf')
			distRight = heaters[idx] - house if idx <= len(heaters) - 1 else float('inf')
			result = max(result, min(distRight, distLeft))
		return result


	# Search the insert index of house in nums
	def searchInsert(self, nums, house):
		l, r = 0, len(nums) - 1
		while l <= r:
			mid = l + (r - l) / 2
			if nums[mid] == house:
				return mid
			elif nums[mid] < house:
				l = mid + 1
			else:
				r = mid - 1
		return l


	# Discussion's solution
	def findRadius(self, houses, heaters):
		houses.sort()
		heaters.sort()
		i, res = 0, 0
		for house in houses:
			while i < len(heaters) - 1 and heaters[i] + heaters[i + 1] <= house * 2:
				i += 1
			res = max(res, abs(heaters[i] - house))
		return res