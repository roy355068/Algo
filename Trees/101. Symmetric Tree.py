# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # recursive solution
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.helper(root.left, root.right)
    """
    recursively check the equality of the symmetric element pairs
    """
    def helper(self, l, r):
        # if one of the node is null, check if another one is also null or not.
        if not l or not r:
            return l == r
        # Return False if the symmetric nodes are not having the same value
        if l.val != r.val:
            return False
        # Checking the symmetric nodes
        return self.helper(l.left, r.right) and self.helper(l.right, r.left)

    """
    Iterative solution.
    Use a queue to store the nodes
    """
    def isSymmetricIterative(self, root):
        from Queue import Queue
        q = Queue()
        q.put(root)
        q.put(root)
        while not q.empty():
            t1 = q.get()
            t2 = q.get()
            if not t1 and not t2:
                continue
            elif not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            # Make sure that each nodes in pairs that needed to be compared
            # are next to each other
            q.put(t1.left)
            q.put(t2.right)
            q.put(t1.right)
            q.put(t2.left)
        return True
