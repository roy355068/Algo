# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # pass in a list in order to avoid using global/instance variable
        res = [float('-inf')]
        self.helper(res, root)
        return res[0]

    def helper(self, res, node):
        if not node:
            return 0
        # if the maxSum of subtree is negative, then the sum is guranteed to
        # be smaller if add those values at the node, so use a zero to reset it
        l = max(0, self.helper(res, node.left))
        r = max(0, self.helper(res, node.right))
        # update the maxPathSum using res list
        # the max would be max itself, or current node's value plus the left and right
        # path sums
        res[0] = max(res[0], node.val + l + r)
        # For the parent node of "node", once the traversal going down, it cannot go upward
        # again. l and r stand for maxSum when traverse down left or right subtree,
        # so that the "parent" node could only take one path down
        return node.val + max(l, r)
