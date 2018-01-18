class Solution(object):
    # Concise way. Slice off the inorder array so that we don't need to calculate
    # the correct offset of preorder when finding next root
    def buildTree(self, preorder, inorder):
        return self.helper(preorder, inorder, 0)

    def helper(self, preorder, inorder, preStart):
        if not inorder:
            return None
        root = TreeNode(preorder[preStart])
        rootIndex = inorder.index(root.val)
        root.left = self.helper(preorder, inorder[:rootIndex], preStart + 1)
        root.right = self.helper(preorder, inorder[rootIndex + 1:], preStart + rootIndex + 1)
        return root


    # Verbose way. Needs to calculate the offset by
    # adding  rootIndex - iStart + 1 to  starting point of preOrder
    def buildTree(self, preorder, inorder):
        return self.helper(preorder, inorder, 0, len(inorder) - 1, 0)

    def helper(self, preorder, inorder, iStart, iEnd, pStart):
        if iStart > iEnd:
            return None
        root = TreeNode(preorder[pStart])
        index = inorder.index(root.val)
        root.left = self.helper(preorder, inorder, iStart, index - 1, pStart + 1)
        root.right = self.helper(preorder, inorder, index + 1, iEnd, pStart + (index - iStart + 1))
        return root
