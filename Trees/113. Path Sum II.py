# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Queue import Queue

class Solution(object):
    # BFS with a queue
    """
    Use temp + [curr.left.val] to avoid update the temp before we can
    assure that the node and path is valid

    """
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if root:
            q = Queue()
            q.put((root, root.val, [root.val]))
            while not q.empty():
                curr, currVal, temp = q.get()
                if not curr.left and not curr.right and currVal == sum:
                    res.append(temp[:])
                if curr.left:
                    q.put((curr.left, currVal + curr.left.val, temp + [curr.left.val]))
                if curr.right:
                    q.put((curr.right, currVal + curr.right.val, temp + [curr.right.val]))
        return res

    # Recursive DFS
    def pathSumRecursiveDFS(self, root, sum):
        res = []
        if root:
            self.helper(root, sum, [], res)
        return res

    def helper(self, node, sum, temp, res):
        if node:
            temp.append(node.val)
            if not node.left and not node.right and sum == node.val:
                res.append(temp[:])
            self.helper(node.left, sum - node.val, temp, res)
            self.helper(node.right, sum - node.val, temp, res)

    # Iterative DFS with a stack
    def pathSumIterativeDFS(self, root, sum):
        res = []
        if root:
            stack = [(root, root.val, [root.val])]
            while stack:
                curr, currVal, temp = stack.pop()
                if not curr.left and not curr.right and currVal == sum:
                    res.append(temp[:])
                if curr.right:
                    stack.append((curr.right, currVal + curr.right.val, temp + [curr.right.val]))
                if curr.left:
                    stack.append((curr.left, currVal + curr.left.val, temp + [curr.left.val]))
        return res
