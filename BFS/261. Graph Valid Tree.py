from collections import *
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n == 1:
            return True
        q = deque()
        graph = [set() for _ in xrange(n)]
        visited = [0 for _ in xrange(n)]

        for e in edges:
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])

        # start BFS from node 0
        q.append(0)
        # set it to temp visited
        visited[0] = 1

        while q:
            curr = q.popleft()
            for node in graph[curr]:
                # if the node is met in the traversal start from other nodes,
                # we can know from the bi-directional property of UDG that there's a cycle
                if visited[node] == 1:
                    return False
                # else if the node hadn't been visited, push it into queue and label it as
                # temporary visited
                elif visited[node] == 0:
                    visited[node] = 1
                    q.append(node)

            # visit is completed, will never re-visit in the bfs
            visited[curr] = 2
        # if there's still some node in the graph that hasn't been
        # visited, then we know that there's more than one connected component
        # hence the graph is not a tree
        return False if 0 in visited else True
