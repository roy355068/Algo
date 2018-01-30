class Solution(object):

	def minDepth(self, root):
		if not root:
			return 0
		if l == 0 or r == 0:
			return 1 + (r if r != 0 else l)
		return 1 + min(r, l)