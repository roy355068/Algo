class Solution(object):
    def buildTree(self, inorder, postorder):
        # Verbose way
        n = len(inorder)
        return self.helper(inorder, postorder, 0, n - 1, n - 1)

    def helper(self, inorder, postorder, iStart, iEnd, pEnd):
        if iStart > iEnd:
            return None
        root = TreeNode(postorder[pEnd])
        index = inorder.index(root.val)
        root.left = self.helper(inorder, postorder, iStart, index - 1, pEnd - (iEnd - index + 1))
        root.right = self.helper(inorder, postorder, index + 1, iEnd, pEnd - 1)
        return root


    # Concise way. But the answer is incorrect when the tree is not complete.
    # Guess the issue is related to the tree structure
    def buildTree(self, inorder, postorder):
        return self.helper(inorder, postorder, len(postorder) - 1)

    def helper(self, inorder, postorder, postEnd):
        if not inorder:
            return None
        root = TreeNode(postorder[postEnd])
        index = inorder.index(root.val)
        root.right = self.helper(inorder[index + 1:], postorder, postEnd - 1)
        root.left = self.helper(inorder[:index], postorder, postEnd - index - 1)
        return root
