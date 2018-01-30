# question 1
# define a binary tree class

class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:

    def __init__(self):
        self.root = None

# question 2
# define a method that returns the string representation of a binary tree
#      a
#     / \
#    b   c
#       /
#      d
# return "(Tree a (Tree b None None) (Tree c (Tree d None None) None))"
# if given None as the input, just return "None"

def solution(root):
    res = []
    dfs(root, res)
    return "".join(res)

def dfs(node, res):
    if not node:
        res.append("None")
        return
    res.append("(Tree " + str(node.val) + " ")

    dfs(node.left, res)
    res.append(" ")
    dfs(node.right, res)
    res.append(")")

# def solution(root):
#     res = []
#     dfs(root, res)
#     # return a string
#     return "".join(res)
#
# def dfs(node, res):
#     if not node:
#         res.append("None")
#         return
#
#     res.append("(Tree " + str(node.val) + " ")
#     dfs(node.left, res)
#     res.append(" ")
#     dfs(node.right, res)
#     res.append(")")

# test your method
# construct a binary tree
# and print out its string representation using your solution function

# a,  b,  c,  d
# 10, 20, 30, 40
root = TreeNode(10)
root.left = TreeNode(20)
root.right = TreeNode(30)
root.right.left = TreeNode(40)

# print solution(root)


root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(5)
import collections
class Solution(object):
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        self.dfs(root, res)
        return "".join(res)

    def dfs(self, node, res):
        if not node:
            res.append("None,")
        else:
            res.append(str(node.val) + ",")
            self.dfs(node.left, res)
            self.dfs(node.right, res)

    def deserialize(self, data):
        q = collections.deque()
        data = data.split(",")
        for d in data:
            q.append(d)
        return self.buildTree(q)

    def buildTree(self, q):
        curr = q.popleft()
        if curr == "None":
            return None
        else:
            node = TreeNode(int(curr))
            node.left = self.buildTree(q)
            node.right = self.buildTree(q)
            return node

x = Solution()
print x.serialize(root2)
