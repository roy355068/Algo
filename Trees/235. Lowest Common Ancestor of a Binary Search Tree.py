class Solution(object):
	def lowestCommonAncestor(self, root, p, q):
		if not root:
			return None
		while not p.val <= root.val <= q.val and not q.val <= root.val <= p.val:
			root = root.right if p.val > root.val else root.left
		return root