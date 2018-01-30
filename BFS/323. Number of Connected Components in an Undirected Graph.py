class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = [[] for _ in xrange(n)]
        visited = [False for _ in xrange(n)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        res = 0
        for vertex in xrange(n):
            if not visited[vertex]:
                # if found a not visited vertex, use that vertex as starting point of BFS
                # and increment res by one because previous cc has been visited completely
                res += 1
                q = collections.deque()
                q.append(vertex)

                # after BFS, all the connected nodes in that individual connected
                # component is visited at once
                while q:
                    curr = q.popleft()
                    visited[curr] = True
                    for neighbor in graph[curr]:
                        if not visited[neighbor]:
                            visited[neighbor] = True
                            q.append(neighbor)
        return res
