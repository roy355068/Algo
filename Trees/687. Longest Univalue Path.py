# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = [0]
        self.helper(res, root, root.val)
        return res[0]

    def helper(self, res, node, nodeVal):
        if not node:
            return 0
        l = self.helper(res, node.left, node.val)
        r = self.helper(res, node.right, node.val)
        # Major difference between this question and q.124
        # update the maxResult with only # of edges
        res[0] = max(res[0], l + r)
        # and note that we only need to count the value from subtree
        # when the currently considered node has the same value with
        # its parent node, otherwise the "path" is not continuous
        # hence the # of edges would be zero
        if node.val == nodeVal:
            return 1 + max(l, r)
        return 0
