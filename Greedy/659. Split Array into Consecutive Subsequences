# You are given an integer array sorted in ascending order (may contain duplicates), you need to split them into several subsequences, where each subsequences consist of at least 3 consecutive integers. Return whether you can make such a split.

# Example 1:
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3
# 3, 4, 5

# Example 2:
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3, 4, 5
# 3, 4, 5

# Example 3:
# Input: [1,2,3,4,4,5]
# Output: False

# input in range of [1, 10000]

class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
        	return False
        endList, freq = {}, {}
        for i in nums:
        	freq[i] = freq.get(i, 0) + 1
        for i in nums:
        	if freq[i] == 0:
        		continue
        	elif endList.get(i, 0) > 0:
        		endList[i] -= 1
        		endList[i + 1] = endList.get(i + 1, 0) + 1
        	elif freq.get(i + 1, 0) > 0 and freq.get(i + 2, 0) > 0:
        		freq[i + 1] -= 1
        		freq[i + 2] -= 1
        		endList[i + 3] = endList.get(i + 3, 0) + 1
        	else:
        		return False
        	freq[i] -= 1
        return True


