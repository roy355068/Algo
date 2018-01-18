class Solution(object):
    def maxDepth(self, root):
        # if the node is null, return 0 since the distance between current node
        # to leaves is zero
        if not root:
            return 0
        # calculate the maxDepth for left and right subtree, respectively
        l = self.maxDepth(root.left)
        r = self.maxDepth(root.right)
        # take the maxDepth in the subtrees and add one, which indicates the
        # current depth
        return 1 + max(l, r)
