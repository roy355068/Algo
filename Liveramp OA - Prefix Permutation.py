def prefix_permute(nums):
	# running total of values and indices
	# if the two sums are equal meaning that the 1 to p th elements contains number 1 to p
	indices, values, res = 0, 0, 0
	for i in xrange(len(nums)):
		indices += i + 1
		values += nums[i]
		if indices == values:
			res += 1
	return res

	# Or keep tracking of the min and max before and on the current index, if min is 1 and max is the 
	# number of index, then it's a prefix permutation.
# print prefix_permute([2, 1, 3, 5, 4])