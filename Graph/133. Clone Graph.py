# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
from collections import deque
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        dic = {}
        return self.helper(node, dic)

    # DFS solution with a dictionay to facilitate the process
    # O(N) for time and space
    # Note that node's label is unique in the graph, so it's
    # perfect scenario to use hashMap to store the key value pair
    def helper(self, node, dic):
        if not node:
            return None
        elif node.label in dic:
            return dic[node.label]
        # reconstruct the node and put it into dic
        cloned = UndirectedGraphNode(node.label)
        dic[node.label] = cloned

        # traverse the graph in dfs manner starting with
        # the neighbors of the current node, then add
        # the reconstructed neighbors' node into the neighbors list
        for n in node.neighbors:
            cloned.neighbors.append(self.helper(n, dic))
        return cloned

    # BFS. O(N) for time and space (queue and dict)
    def cloneGraph(self, node):
        if not node:
            return None
        q, dic = deque(), {}
        # new root for the cloned graph
        root = UndirectedGraphNode(node.label)
        dic[root.label] = root
        q.append(node)

        while q:
            curr = q.popleft()
            for n in curr.neighbors:
                if n.label not in dic:
                    dic[n.label] = UndirectedGraphNode(n.label)
                    q.append(n)
                # reconstruct the neighbors list for the newly created node
                dic[curr.label].neighbors.append(dic[n.label])
        return root
