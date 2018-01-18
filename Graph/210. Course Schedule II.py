class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Time Complexity = O(|V| + |E|), Space Complexity = O(V)

        graph = [[] for _ in xrange(numCourses)]
        visited = [0 for _ in xrange(numCourses)]
        res = []
        for p in prerequisites:
            graph[p[1]].append(p[0])

        for i in xrange(numCourses):
            if not self.dfs(graph, visited, i, res):
                return []
        return list(reversed(res))

    def dfs(self, graph, visited, course, res):
        if visited[course] == -1:
            return False
        elif visited[course] == 1:
            return True
        visited[course] = -1

        for c in graph[course]:
            if not self.dfs(graph, visited, c, res):
                return False

        visited[course] = 1
        res.append(course)
        return True
