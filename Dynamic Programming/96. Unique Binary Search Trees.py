# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        # https://discuss.leetcode.com/topic/8398/dp-solution-in-6-lines-with-explanation-f-i-n-g-i-1-g-n-i
        """
			Use the concept in the post above, we can define two functions: g and f

			g(n) : the number of unique BST for n
			f(i, n) : the number of unique BST using i, where 1 <= i <= n, as root

			g(n) would be the ultimate answer in this problem
			g[0] = g[1] = 1 because the number of ways of generating unique BST is one
			g(n) = f(1, n) + f(2, n) + ...... + f(n, n)

			f(i, n) could be viewed as g(i - 1) * g(n - i)
			use i as root will divide the array into [1 : i - 1] and [i + 1 : n]
			so the f(i, n) is the cartesian product of g(i - 1) and g(n - j)
			which means the number of the unique subtrees.

			so substitute the f(i, n) into the g(n) equation:
			g(n) = g(0) * g(n - 1) + g(1) * g(n - 2) + ....... + g(n - 1) * g(0)

        """
        g = [1 if x == 0 or x == 1 else 0 for x in xrange(n + 1)]
        for i in xrange(2, n + 1):
        	for j in xrange(1, i + 1):
        		g[i] += g[j - 1] * g[i - j]
        return g[n]

