class Solution(object):
    def morrisInorderTraversal(self, root):
        res = []
        curr, prev = root, None
        while curr:
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                # indicate that this node's right child is linking the
                # current node due to the stopping while condition
                # so trim the right tree to restore the tree's original
                # structure, then do the same thing as in
                # the condition of no left child
                if prev.right == curr:
                    prev.right = None
                    res.append(curr.val)
                    curr = curr.right
                # if the prev's right child is not linking to curr node
                # link them in order to visit back the current node
                # after finishing traversal in left subtree
                else:
                    prev.right = curr
                    curr = curr.left
        return res

    def morrisPreorderTraversal(self, root):
        res = []
        curr, prev = root, None
        while curr:
            if not curr.left:
                res.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right

                if prev.right == curr:
                    prev.right = None
                    curr = curr.right

                else:
                    prev.right = curr
                    # only difference from the inorder traversal
                    res.append(curr.val)
                    curr = curr.left

    def morrisPostorderTraversal(self, root):
        res = []
        curr, prev = root, None
        while curr:
            if not curr.right:
                res.append(curr.val)
                curr = curr.left
            else:
                prev = curr.right
                while prev.left and prev.left != curr:
                    prev = prev.left

                if prev.left == curr:
                    prev.left = None
                    curr = curr.left
                else:
                    prev.left = curr
                    res.append(curr.val)
                    curr = curr.right
        return list(reversed(res))
