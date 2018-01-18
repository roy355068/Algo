# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        BFS, level-order traversal using deque to pop from left in constant
        time.

        Because I'm traversing in level-order, I always add the last element
        (which is the rightmost node in each layer) to the result
        """
        dq, res = deque(), []
        if root:
            dq.append(root)
            while dq:
                res.append(dq[-1].val)
                for _ in xrange(len(dq)):
                    curr = dq.popleft()
                    if curr:
                        if curr.left:
                            dq.append(curr.left)
                        if curr.right:
                            dq.append(curr.right)
        return res

    def rightSideViewDFS(self, root):
        rights = {}
        maxDepth = -1
        stack = [(0, root)]
        while stack:
            depth, node = stack.pop()
            if node:
                maxDepth = max(maxDepth, depth)
                if depth not in rights:
                    rights[depth] = node.val
                stack.append((depth + 1, node.left))
                stack.append((depth + 1, node.right))
        return [rights[i] for i in xrange(maxDepth + 1)]
