class Solution(object):
	def kthSmallest(self, root, k):

		Iterative way
		stack = []
		while root or stack:
			while root:
				stack.append(root.val)
				root = root.left
			root = stack.pop()
			k -= 1
			if k == 0:
				break
			root = root.right
		return root.val


	def recursive(self, root, k):
		arr = []
		self.inorder(root, arr)
		return arr[k - 1]
	def inorder(self, node, arr):
		if not node:
			return 
		self.inorder(node.left)
		arr.append(node.val)
		self.inorder(node.right)

