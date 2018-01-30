import collections
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        res = []
        if endWord not in wordList:
            return res
        chars = [chr(i) for i in xrange(ord('a'), ord('z') + 1)]
        count = 1
        wordLen = len(beginWord)
        q = collections.deque()
        q.append(beginWord)

        # keep track of the predecessor(s) of each string
        predecessor = collections.defaultdict(list)
        predecessor[beginWord] = None
        distance = {w : float('inf') for w in wordList}
        distance[beginWord] = 0

        # in word ladder, we can use a visited set to keep track of
        # what nodes we have visited, and we only need one single shortest path

        # But in this question, we need to find multiple path. As the result
        # we need to visit some nodes multiple times since it might in multiple different paths
        # so the visited strategy won't work here, instead we keep updating the distance map

        while q:
            for _ in xrange(len(q)):
                curr = q.popleft()
                for i in xrange(wordLen):
                    for c in chars:
                        temp = curr[:i] + c + curr[i + 1:]
                        if temp in wordList:
                            # if the step count is larger than curr distance of temp, ignore it
                            if count > distance[temp]:
                                continue
                            # else if there's a shorter path to temp, update the distance
                            elif count < distance[temp]:
                                    q.append(temp)
                                    distance[temp] = count

                            if temp != curr:
                                predecessor[temp].append(curr)
            count += 1
        self.backtrack(res, collections.deque(), predecessor, endWord, count - 1)
        return res

    # use the predecessor map to generate the sequence of possible paths
    def backtrack(self, res, temp, predecessor, string, count):
        # if the len of temp is larger than the minimum allowed steps, directly return
        if len(temp) > count:
            return

        temp.appendleft(string)
        # if the prev[string] is None, means that we reach the beginWord, append the temp result
        # remember to pop the temp list for further backtracking
        if predecessor[string] == None:
            res.append(list(temp))
            temp.popleft()
            return

        for pre in predecessor[string]:
            self.backtrack(res, temp, predecessor, pre, count)
        temp.popleft()
