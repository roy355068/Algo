
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