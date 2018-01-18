# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        return self.BFS(root)
        return self.recursiveDFS(root)

    def BFS(self, root):
        dq = deque()
        res = []
        if root:
            dq.append(root)
            while dq:
                res.append(max(dq, key = lambda x : x.val).val)
                for _ in xrange(len(dq)):
                    curr = dq.popleft()
                    if curr:
                        if curr.left:
                            dq.append(curr.left)
                        if curr.right:
                            dq.append(curr.right)
        return res


    def recursiveDFS(self, root):
        res = []
        self.helper(root, res, 0)
        return res
    def helper(self, node, res, depth):
        if not node:
            return
        # if the depth is larger than the size of the result list
        # means that the program reached a deeper layer of the tree,
        # hence expand the list
        if depth == len(res):
            res.append(node.val)
        # else, update the list element at the "depth" index with a maximum
        # value of current node or previous max val node
        else:
            res[depth] = max(res[depth], node.val)
        self.helper(node.left, res, depth + 1)
        self.helper(node.right, res, depth + 1)
