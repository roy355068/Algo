from collections import *

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        # the concept could start from 1d array
        # the root will be the element in the middle if the # of ele is odd
        # or the middle two if the # is even
        # so we could work in the same way that start from the leaves(ends)
        # and move into the center. If the n is <= 2 that means we got our roots

        # corner case
        if n == 1:
            return [0]
        graph = [set() for _ in xrange(n)]
        q = deque()

        for e in edges:
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])

        # use the length of [neighbors] to represent the degree of the node
        leaves = [i for i in xrange(n) if len(graph[i]) == 1]

        while n > 2:
            for leaf in leaves:
                node = graph[leaf].pop
                graph[node].remove(leaf)
                if len(graph[node]) == 1:
                    
