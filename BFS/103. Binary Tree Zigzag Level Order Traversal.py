# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import *

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        res = []
        q = deque()
        q.append(root)
        isLeft = True

        while q:
            temp = deque()
            for _ in xrange(len(q)):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                if isLeft:
                    temp.append(curr.val)
                else:
                    temp.appendleft(curr.val)
            isLeft = not isLeft
            res.append(list(temp))

        return res
