# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        # self.iterativeDFSWithStack(root)
        # self.RecursiveDFS(root)

    def flattenMorrisTraversal(self, root):
        # Morris Traversal
        # O(N) time complexity, O(1) space complexity
        # first find the prev node of the right subtree of the node
        # in the left subtree so that we could revisit the right subtree
        # after traverse down the left one
        curr = root
        while curr:
            # if there's left subtree, find the prev node
            # otherwise move down to the right subtree
            if curr.left:
                prevInLeft = curr.left
                # find the rightmost node in the left subtree
                while prevInLeft.right:
                    prevInLeft = prevInLeft.right
                # connect prev with root's right subtree, so that
                # we could revisit in the following traversal
                prevInLeft.right = curr.right
                curr.right = curr.left
                # trim left child!!!
                curr.left = None
            curr = curr.right


    def iterativeDFSWithStack(self, root):
        if root:
            stack = [root]
            while stack:
                curr = stack.pop()
                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
                if stack:
                    curr.right = stack[-1]
                # Trim the left subtree to be None based on the spec
                curr.left = None

    # Recursive DFS solution
    # O(N Log N) for time complexity, because every node will be visited
    # Log N time when finding the leaf of the "pasted right subtree"
    # O(N) for space complexity for recursion stack
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        # flatten left and right subtrees based on the algo below
        self.flatten(root.left)
        self.flatten(root.right)

        # store the original right subtree and paste it back after
        # append the left subtree to the root
        rightSub = root.right
        if root.left:
            # append the left subtree to the right pointer of the root
            # and make the pointer points to null
            # to fulfill the requirement of the question
            root.right = root.left
            root.left = None
            # if the original right subtree is not empty, then
            # append it back to the end of the "current" right subtree
            if rightSub:
                # move all the way down to the leaf of current right subtree
                while root.right:
                    root = root.right
                # append !
                root.right = rightSub
