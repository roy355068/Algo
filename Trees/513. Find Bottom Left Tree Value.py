# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # 1. the most naive way is to do level-order traversal and check
    #    the leftmost element in the deepest depth of the tree
    # 1.5 Slightly optimized way to do 1. is to do the level-order in a
    #    "reversed" way!
    #     Start putting node from right to left instead of starting from left
    #    in this way we can assure that the last element pull from queue
    #    is the leftmost subtree(node)
    # 2. can use a dictionary to keep { depth : [node.vals] } of each layer.
    #    since we can do the recursion from left to right subtrees, we can
    #    assure that the leftmost element in each value in dic is the leftmost
    #    TreeNode
    def findBottomLeftValueSubOptimal(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        dic = {}
        maxDepth = self.helper(root, dic, 0, 0)
        return dic[maxDepth][0]

    def helper(self, node, dic, depth, maxDepth):
        if not node:
            return maxDepth
        # since the first element in value of dic would away be the leftmost
        # node in each layer, we only need to handle the condition when
        # there's no depth as key in dic
        if depth not in dic:
            dic[depth] = [node.val]
        maxDepth = max(depth, maxDepth)
        return max(self.helper(node.left, dic, depth + 1, maxDepth), \
                    self.helper(node.right, dic, depth + 1, maxDepth))

    def findBottomLeftValueOptimizedLevelOrder(self, root):
        from Queue import Queue
        q = Queue()
        q.put(root)
        while not q.empty():
            curr = q.get()
            if curr.right:
                q.put(curr.right)
            if curr.left:
                q.put(curr.left)
        return curr.val
    # 3. an optimized way to do 2. Constant space complexity
    # since we only need the deepest depth's first element of the list
    # we may use a two-items list to store the current depth and node.val.
    # if the depth is larger than the depth recorded in the list,
    # we update the list till we reach the bottom of the tree
    def findBottomLeftValue(self, root):
        # set initial depth as 1 to make the update condition fulfilled in
        # the helper function
        return self.find(root, 1, [0, 0])

    def find(self, node, depth, res):
        if not node:
            return
        # this statement means that the current depth is the deeper depth
        # than current recorded one, so update the res list
        if depth > res[0]:
            res[0], res[1] = depth, node.val
        # Following recursions are used to update the res list
        # so no need to assign their value to variables
        self.find(node.left, depth + 1, res)
        self.find(node.right, depth + 1, res)
        return res[1]
