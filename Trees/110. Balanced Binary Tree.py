# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root) != -1
    """
    use this helper function to recursively find the maximum depth
    of the two subtrees.
    If there's an inbalance in the subtree, return -1, and that -1 would
    propagate toward the root and return by the main function
    """
    def helper(self, node):
        if not node:
            return 0
        l = self.helper(node.left)
        r = self.helper(node.right)
        if l == -1 or r == -1 or abs(l - r) > 1:
            return -1
        # Return the maximal depth in the subtree because a tree is balanced or
        # not is determined by the maxDepth
        return 1 + max(l, r)
