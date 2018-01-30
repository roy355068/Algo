class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        visited = [False for _ in xrange(n)]
        graph = [[] for _ in xrange(n)]

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        res = 0
        for vertex in xrange(n):
            if not visited[vertex]:
                res += 1
                self.dfs(graph, visited, vertex)
        return res

    def dfs(self, graph, visited, start):
        # here we need to note the sequence of labeling node as visited
        # label it too early will cause the connected component to break
        # and has a unexpected larger result

        if not visited[start]:
            visited[start] = True
            for neighbor in graph[start]:
                self.dfs(graph, visited, neighbor)
        
