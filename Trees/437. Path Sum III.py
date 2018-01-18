# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.helper(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def helper(self, node, sum):
        if not node:
            return 0
        return (1 if node.val == sum else 0) + \
                self.helper(node.left, sum - node.val) + \
                self.helper(node.right, sum - node.val) \
