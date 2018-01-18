class Solution(object):
	def lowestCommonAncestor(self, root, p, q):
		if not root or root == p or root == q:
			return root
		left = self.lowestCommonAncestor(root.left, p, q)
		right = self.lowestCommonAncestor(root.right, p, q)
		if left and right:
			return root
		return left if left else right





	def lowestCommonAncestorIterative(self, root, p, q):
		stack = [ root ]
		parents = { root : None }
		while not p in parents or not q in parents:
			node = stack.pop()
			if node.left:
				parents[node.left] = node
				stack.append(node.left)
			if node.right:
				parents[node.right] = node
				stack.append(node.right)
		ancestors = set()
		while p:
			ancestors.add(p)
			p = parents[p]
		while q not in ancestors:
			q = parents[q]
		return q

