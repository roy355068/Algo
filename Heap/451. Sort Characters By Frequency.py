# Given a string, sort it in decreasing order based on the frequency of characters.

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        """
		My solution, use a dictionary (HashMap) to store the frequency of each chars
		Then transform the dictionary to list and sort it by the freqencies.
		Space complexity = O(n)
        """
        dic = {}
        for c in s:
            dic[c] = dic.get(c, 0) + 1
        lst = []
        for (k, v) in dic.items():
            lst.append([k, v])
        lst.sort(key = lambda x : x[1], reverse = True)
        for i in xrange(len(lst)):
            lst[i] = lst[i][1] * lst[i][0]
        return "".join(lst)

        