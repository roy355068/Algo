class Solution(object):

	def cloneGraph(self, node):
		if not node:
			return None
		# use HashMap to store the nodes that has showed up
		root = UndirectedGraphNode(node.label)
		dic = {}
		dic[root.label] = root
		# push the original root to the queue for traversal
		q = collections.deque()
		q.append(node)

		while q:
			curr = q.popleft()
			for n in curr.neighbors:
				# if n.label is not in dic, create the entry 
				# with the label and the new node, then append
				# the original neighbor node for further traversal
				if n.label not in dic:
					dic[n.label] = UndirectedGraphNode(n.label)
					q.append(n)
				# append the newly created neighbor nodes to the newly created node
				dic[curr.label].neighbors.append(dic[n.label])
		return root