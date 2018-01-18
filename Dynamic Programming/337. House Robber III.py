class Solution(object):
    # Recursively compute the max with two condition
    # rob current house and recursively rob its grandchildren
    # or don't rob the current house but rob its children
    # O(2 ^ N) time complexity due to the fact that

    # For each tree node tn at depth d, let T(d) be the number of times
    # the rob function will be called on it. Then we have T(d) = T(d - 1) + T(d - 2).
    # This is because rob will be called on tn either from its parent (at depth d - 1)
    # or its grandparent (at depth d - 2)
    def NaiveRob(self, root):
        if not root:
            return 0
        val = 0
        # construct the val for robbing current house
        if root.right:
            val += self.NaiveRob(root.right.right) + self.NaiveRob(root.right.left)
        if root.left:
            val += self.NaiveRob(root.left.left) + self.NaiveRob(root.left.right)

        # take the max of either rob the current house and its grandchildren
        # or rob the children of the current house only
        return max(val + root.val, self.NaiveRob(root.left) + self.NaiveRob(root.right))

    # Use a dictionary to store the node that had been visited so that we don't
    # need to recompute the computed results => A DP problem
    # O(N) for both time and space complexity
    def improvedRob(self, root):
        return self.helper(root, {})

    def helper(self, node, dic):
        if not node:
            return 0
        elif node in dic:
            return dic[node]
        # compute the results of the two scenarios
        val = 0
        if node.left:
            val += self.helper(node.left.left, dic) + self.helper(node.left.right, dic)
        if node.right:
            val += self.helper(node.right.right, dic) + self.helper(node.right.left, dic)
        val = max(val + node.val, self.helper(node.left, dic) + self.helper(node.right, dic))
        dic[node] = val
        return val

    # Use an array instead of a big dictionary to store the dp results
    # O(N) for both time and space (call stack of recursion) complexity
    def optimizedRob(self, root):
        return max(self.helper(root))

    # The return value would have two elements in it
    # The first element is robbing the current house
    # while second one stands for not robbing the current house
    def helper(self, node):
        if not node:
            return [0, 0]
        left = self.helper(node.left)
        right = self.helper(node.right)
        res = [0, 0]
        # if robbing the current house, then we should take the value
        # that indicates not robbing the children nodes
        res[0] = node.val + left[1] + right[1]
        # if doesn't rob the current house, then take the max of the two
        # scenarios and add up the left and right subtree's results
        res[1] = max(left) + max(right)
        return res
