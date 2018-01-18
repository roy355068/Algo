class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # The map maps the char to indices of that char in the string
        tMap = {}
        for i in xrange(len(t)):
        	char = t[i]
        	if char not in tMap:
        		tMap[char] = []
        	tMap[char].append(i)
        # prev is a variable keep tracking the prev char position in t that has been matched in t
        prev = 0
        for c in s:
        	if c not in tMap:
        		return False
        	else:
                # so i is basically checking the position of current char in s in t
        		i = bisect.bisect_left(tMap[c], prev)
                # if the position of c in t is equal to the length of the list of indices
                # meaning that the order in s is not matching the pattern in t
        		if i == len(tMap[c]):
        			return False
        		prev = tMap[c][i] + 1
        return True
