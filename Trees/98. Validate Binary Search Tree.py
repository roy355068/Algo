
class Solution(object):
	def isValidBST(self, root):
		return self.validate(root, float('inf'), float('-inf'))


	"""
	maxVal and minVal is the upper and lower limits the child nodes could reach
	in the right subtree, we should set the lower limits to node.val 
	to make sure that every nodes in right subtrees has values that are greater than the root
	in the feft subtree, we should set the upper limits to node.val
	"""
	def validate(self, node, maxVal, minVal):
		if not node:
			return True
		
		if node.val <= minVal or node.val >= maxVal:
			return False

		else:
			return self.validate(node.left, node.val, minVal) and self.validate(node.right, maxVal, node.val)


	def iterative(self, root):
		stack, prev = [], None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev and root.val <= prev.val:
                return False
            prev = root
            root = root.right
        return True


