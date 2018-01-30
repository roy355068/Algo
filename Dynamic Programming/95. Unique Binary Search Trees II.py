
class Solution(object):

    # Brute force : recursively generate all the BStrees
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
        	return []
        return self.helper(1, n)

    def helper(self, start, end):
    	if start > end:
    		return [None]
    	lst = []
    	for i in xrange(start, end + 1):
    		leftList = self.helper(start, i - 1)
    		rightList = self.helper(i + 1, end)
    		for l in leftList:
    			for r in rightList:
    				root = TreeNode(i)
    				root.left = l
    				root.right = r
    				lst.append(root)
    	return lst

    # Dynamic Programming Solution
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        dp = collections.defaultdict(list)
        dp[0].append(None)
        dp[1].append(TreeNode(1))
        for i in xrange(2, n + 1):
            for j in xrange(1, i + 1):
                leftList = dp[j - 1]
                rightList = dp[i - j]

                for l in leftList:
                    for r in rightList:
                        root = TreeNode(j)
                        root.left = l
                        # the nodes on the right will need to shift all of their values by offset j
                        root.right = self.clone(r, j)
                        dp[i].append(root)
        return dp[n]

    def clone(self, node, offset):
        if not node:
            return None
        newNode = TreeNode(node.val + offset)
        newNode.left = self.clone(node.left, offset)
        newNode.right = self.clone(node.right, offset)
        return newNode
