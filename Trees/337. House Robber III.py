# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Use an array instead of a big dictionary to store the dp results
    # O(N) for both time and space (call stack of recursion) complexity
    def rob(self, root):
        return max(self.helper(root))

    # The return value would have two elements in it
    # The first element is robbing the current house
    # while second one stands for not robbing the current house
    def helper(self, node):
        if not node:
            return [0, 0]
        left = self.helper(node.left)
        right = self.helper(node.right)
        res = [0, 0]
        # if robbing the current house, then we should take the value
        # that indicates not robbing the children nodes
        res[0] = node.val + left[1] + right[1]
        # if doesn't rob the current house, then take the max of the two
        # scenarios and add up the left and right subtree's results
        res[1] = max(left) + max(right)
        return res
