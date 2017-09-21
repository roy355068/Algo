# Given an array of strings, group anagrams together.

# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
# Return:

# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[
        """
        if not strs:
        	return []

        # Solution 1
        dic = {}
        for s in strs:
        	t = tuple(sorted(s))
        	# or t = str(sorted(s)), 
        	# as long as the key of the dictionary be hashable it should be fine
        	dic.setdefault(t, []).append(s)
        return dic.values()

        # Solution 2
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
        

