# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, 0)

    def helper(self, node, sum):
        # ending condition 1. If there's no node, return 0 (no node.val)
        if not node:
            return 0
        # ending condition 2. If current node is a leave, return the current sum
        # plus current node's value
        if not node.left and not node.right:
            return sum * 10 + node.val
        # Sum up the left subtree and right subtree recursively
        # Return the cumulative sum of the two subtrees
        return self.helper(node.left, sum * 10 + node.val) + \
                self.helper(node.right, sum * 10 + node.val)

    # O(N) for both time and space
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        self.helper(res, [], root)
        return res[0]

    def helper(self, res, temp, node):
        if not node:
            return

        temp.append(node.val)
        if node and not node.left and not node.right:
            multiplier = 10 ** (len(temp) - 1)
            s = 0
            for i in xrange(len(temp)):
                s += temp[i] * multiplier
                multiplier /= 10
            res[0] += s

        self.helper(res, temp, node.left)
        self.helper(res, temp, node.right)
        temp.pop()
