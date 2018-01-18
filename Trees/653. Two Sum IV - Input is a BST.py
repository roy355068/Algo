from collections import deque
class Solution(object):

    # 1st solution, use a set to record the values of nodes that
    # has been visited, and check if the target
    # time : O(N), Space : O(N) given N is the number of nodes
    def findTarget(self, root, k):
        temp = set()
        return self.helper(root, temp, k)

    def helper(self, node, temp, k):
        if not node:
            return False
        if k - node.val in temp:
            return True
        return self.helper(node.left, temp, k) or self.helper(node.right, temp, k)

    # 2nd solution, BFS. Still needs a set to record values
    # but instead of doing it in DFS like in previous solution,
    # this solution use BFS to traverse the tree
    # time : O(N), Space : O(N) given N is the number of nodes
    def findTarget(self, root, k):
        temp = set()
        q = deque()
        q.append(root)
        while q:
            curr = q.pop()
            if k - curr.val in temp:
                return True
            temp.add(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return False
        
    # 3rd solution, parse the BST into an inorder array and linear scan
    # through the whole array since BST would be sorted in an inorder array
