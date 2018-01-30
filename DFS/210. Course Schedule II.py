class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in xrange(numCourses)]
        visited = [0 for _ in xrange(numCourses)]
        res = collections.deque()

        for p in prerequisites:
            graph[p[1]].append(p[0])

        for course in xrange(numCourses):
            if not self.dfs(res, graph, course, visited):
                return []
        return list(res)

    def dfs(self, res, graph, course, visited):
        if visited[course] == 1:
            return True
        elif visited[course] == -1:
            return False
        visited[course] = -1
        for neighbor in graph[course]:
            if not self.dfs(res, graph, neighbor, visited):
                return False
        # all the rest is the same as Course Schedule I
        # note that here we need to add the node in the front of the res
        # because the recursion will ends at the "leaves" of the graph
        # hence the leaves will be added into res in a reversed order
        visited[course] = 1
        res.appendleft(course)
        return True
