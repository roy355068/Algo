from Queue import *
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # list for all alphabets
        charList = [chr(x) for x in xrange(97, 123)]
        # visited used to record the visited words
        visited = set()
        visited.add(beginWord)
        # transform the list into set in order to improve searching (in) performance
        # average case time complexity of 'x in set' is O(1)
        wordSet = set(wordList)
        # A queue used to do the BFS algorithm
        q = Queue()
        q.put(beginWord)
        # res is the number of transformation we need to make to get
        # the beginWord to endWord
        res = 1
        while not q.empty():
        	# in each layer, we only need to 
            for _ in xrange(q.qsize()):
                curr = q.get()
                if curr == endWord:
                    return res
                for i in xrange(len(curr)):
                    for c in charList:
                        temp = curr[:i] + c + curr[i+1:]
                        if temp not in visited and temp in wordSet:
                            visited.add(temp)
                            q.put(temp)
            res += 1
        return 0