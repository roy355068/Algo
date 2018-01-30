class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in xrange(numCourses)]
        inDegree = [0 for _ in xrange(numCourses)]
        q = collections.deque()
        res = []

        for p in prerequisites:
            graph[p[1]].append(p[0])
            inDegree[p[0]] += 1

        for i in xrange(numCourses):
            if inDegree[i] == 0:
                q.append(i)
                res.append(i)
        # the difference between DFS solution is that
        # we don't need to append the node reversely
        # since we done the visits first on the closer nodes
        while q:
            for _ in xrange(len(q)):
                curr = q.popleft()
                for neighbor in graph[curr]:
                    inDegree[neighbor] -= 1
                    if inDegree[neighbor] == 0:
                        q.append(neighbor)
                        res.append(neighbor)
                graph[curr] = []
        return [] if any(graph) else res
