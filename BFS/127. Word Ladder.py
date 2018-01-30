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

    # bidirectional BFS
    # run two simultaneous search forward and backward
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        if endWord not in wordList:
            return 0
        res = 1
        wordLength = len(beginWord)
        beginSet, endSet, visited = set(), set(), set()
        beginSet.add(beginWord)
        endSet.add(endWord)
        while beginSet and endSet:
            # because no matter which end we start with, as long as we can move
            # forward one step in the ladder, then the res can be increment by one
            # once the beginSet is larger than endSet, it will be much
            # efficient to start the search from the smaller set
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet

            # tempSet is for iteration in the newx round
            tempSet = set()
            for string in beginSet:
                for i in xrange(wordLength):
                    for c in xrange(ord('a'), ord('z') + 1):
                        newString = string[:i] + chr(c) + string[i + 1:]
                        if newString in endSet:
                            return res + 1
                        if newString not in visited and newString in wordList:
                            visited.add(newString)
                            tempSet.add(newString)
            beginSet = tempSet
            res += 1
        return 0
