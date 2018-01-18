# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import *

class Solution(object):
    # BFS. O(N) for both time and space complexity
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        q = deque()
        q.append(root)
        res = []

        while q:
            res.append(q[-1].val)
            for _ in xrange(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return res

    # DFS
    def rightSideView(self, root):
        res = []
        self.dfs(res, root, 0)
        return res


    # the logic in the dfs helper is that we always start our traversal
    # from the right subtree since it's possible to be the place that the
    # rightmost nodes in each layer.
    # If there's no nodes in the right subtree, then we consider the left subtree

    # Since each layer could only have one node, the second if statement will capture
    # the rightmost node immediately if there's a node which makes the first
    # if fails
    def dfs(self, res, node, depth):
        if not node:
            return None
        if len(res) == depth:
            res.append(node.val)
        self.dfs(res, node.right, depth + 1)
        self.dfs(res, node.left, depth + 1)
