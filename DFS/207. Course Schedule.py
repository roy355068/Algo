class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Build graph with list with indices represented as node and the value
        # list as the node that can reach out through current node
        graph = [[] for _ in xrange(numCourses)]

        # Build a visited list to store each node's status
        # there are three different statues of each individual node
        # -1 : visited in current trip starting from arbitrary node, if
        #      encounters a -1, meaning there's a cycle in graph, hence
        #      it would be impossible to finish all courses
        #  0 : never been visited
        #  1 : had been visited in previous DFS, hence could return directly
        #      without further traversing
        visited = [0 for _ in xrange(numCourses)]

        # each element in prerequisites is storing the directed info about
        # prereq (p[1]) of course p[0], so p[1] is leading out to p[0] in
        # graph representation
        # Note the each index stands for the current node
        for p in prerequisites:
            graph[p[1]].append(p[0])

        # Start DFS traversing on each node
        for node in xrange(len(graph)):
            # if DFS traverse found a cycle, directly return False and
            # terminate algo early
            if not self.dfs(graph, visited, node):
                return False
        return True

    def dfs(self, g, v, curr):
        if v[curr] == -1:
            return False
        elif v[curr] == 1:
            return True
        # set curr node to temporary visited in current trip
        v[curr] = -1
        # Further DFS traversal to traverse all possible path in the graph
        # starting from each connected node to the current node
        for nextCourse in g[curr]:
            if not self.dfs(g, v, nextCourse):
                return False
        # mark the curr node permanently to indicate that this node had
        # been visited in one DFS path, so that the program doesn't need to
        # check again => decrease time complexity
        v[curr] = 1
        return True
