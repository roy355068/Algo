class Solution(object):

	def minDepth(self, root):
		if not root:
			return 0
		res = 1
		q = collections.deque()
		q.append(root)

		while q:
			for _ in xrange(len(q)):
				curr = q.popleft()
				if not curr.left and not curr.right:
					return res
				if curr.left:
					q.append(curr.left)
				if curr.right:
					q.append(curr.right)
			res += 1
		return res
