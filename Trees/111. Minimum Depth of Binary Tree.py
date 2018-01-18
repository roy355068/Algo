# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        """
        recursively find the minimum depth of the tree
        , a noteworthy point is that when there's any subtree is null
        , we should directly add up 1 + l + r since the minimum depth in that
        case would be zero (which is an unexpected result since it's not at
        the leaves yet)
        """
        if not root:
            return 0
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        return 1 + l + r if l == 0 or r == 0 else 1 + min(l, r)

    # Another way to solve it is check if the current node is leaf or not.
    # If it's not leaf and still has at least one children, then by
    # definition we should go down that path to find the minDepth from root to leaves
    def minDepth(self, root):
        if not root:
            return 0
        # increment one to account for current depth
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
