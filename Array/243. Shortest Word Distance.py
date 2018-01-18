class Solution(object):
    def shortestDistance(self, words, word1, word2):
        dist = float('inf')
        idx_1, idx_2 = -1, -1
        for idx, val enumerate(words):
            if val in [word1, word2]:
                if val == word1:
                    idx_1 = idx
                elif val == word2:
                    idx_2 = idx
                if idx_1 != -1 and idx_2 != -1:
                    dist = min(dist, abs(idx_1 - idx_2))
                    # early termination
                    if dist == 1:
                        break
        return dist

    def shortestDistanceIII(self, words, word1, word2):
        index1, index2 = -1, -1
        asWord1 = True
        dist = float('inf')
        for idx, val in enumerate(words):
            if val in [word1, word2]:
                if val == word1 and (word1 != word2 or asWord1):
                    index1 = idx
                elif val == word2 and (word1 != word2 or not asWord1):
                    index2 = idx
                asWord1 = not asWord1

                if index1 != -1 and index2 != -1:
                    dist = min(dist, abs(index2 - index1))
                    if dist == 1:
                        break
        return dist
