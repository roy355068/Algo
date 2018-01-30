class Solution(object):

	def cloneGraph(self, node):
		dic = {}
		return self.dfs(node, dic)

	def dfs(self, node, dic):

		if not node:
			return None

		# if there's node's label in dic, directly return the node
		if node.label in dic:
			return dic[node.label]
		# reconstruct node and add the node into dic
		clone = UndirectedGraphNode(node.lab)
		dic[clone.label] = UndirectedGraphNode(clone.label)

		# dfs
		for n in node.neighbors:
			clone.neighbors.append(self.dfs(n, dic))
		return clone