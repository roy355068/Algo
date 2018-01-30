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
        # since the graph is undirected and is a valid tree,
        # so the nodes that have only one edge will be the leaves
        leaves = [i for i in xrange(n) if len(graph[i]) == 1]

        # the number of root(s) could be up to 2 based on if the
        # number of total nodes is even or odd
        # so once the node number is less than or equal to 2,
        # we have found the root(s)
        while n > 2:
            n -= len(leaves)
            newLeaves = []
            # process the leaves altogether first
            for leaf in leaves:
                # pop out the neighbor from the leaf's neighbors list
                # and remove leaf in the neighbor's neighbors list as well
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                # if the length of the neighbor's neighbors becomes 1
                # meaning that we have found a new leaf in the next level
                if len(graph[neighbor]) == 1:
                    newLeaves.append(neighbor)
            # deep copy from newLeaves to leaves to start next iteration
            leaves = newLeaves[:]
        return leaves
