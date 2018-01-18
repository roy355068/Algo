# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int

        Consecutive means the numbers are continuous
        """
        if not root:
            return 0
        return self.helper(root, root.val, 0)

    def helper(self, node, target, length):
        if not node:
            return length
        length = 1 if node.val != target else length + 1
        return max(length, self.helper(node.left, node.val + 1, length),
                            self.helper(node.right, node.val + 1, length))
