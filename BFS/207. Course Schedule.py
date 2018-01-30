class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Kahn's algorithm (BFS)
        # https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm

        graph = [[] for _ in xrange(numCourses)]
        inDegree = [0 for _ in xrange(numCourses)]
        q = collections.deque()

        # construct the adjacency list and inDegree array
        for p in prerequisites:
            graph[p[1]].append(p[0])
            inDegree[p[0]] += 1

        # push the nodes with zero in-degree into queue
        # to serve them as the starting point of BFS
        for i in xrange(numCourses):
            if inDegree[i] == 0:
                q.append(i)

        while q:
            # visit all the nodes in the same level first
            for _ in xrange(len(q)):
                curr = q.popleft()
                for neighbor in graph[curr]:
                    inDegree[neighbor] -= 1
                    # if inDegree of the node reach 0
                    # then add it to queue to serve as starting node in next round
                    if inDegree[neighbor] == 0:
                        q.append(neighbor)
                # remove all of the edge from curr to its neighbors
                # so that we won't revisit the edge
                graph[curr] = []

        # check if there's any edges left in graph
        # if yes, then the graph has at least one cycle
        # because the cycle will induce "duplicate" arrow
        # toward the node, so we could not remove it comletely from the graph
        return any(graph) == False
