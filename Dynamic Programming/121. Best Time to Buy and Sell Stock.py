# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5

# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0

# In this case, no transaction is done, i.e. max profit = 0.
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
        	return 0
        # Solution 1 (Solution from discussion forum : Kadane's Algorithm!!!!!!)
        """
        	Same as my solution, but only use O(1) space complexity to solve the problem
        """
        currMax, soFarMax = 0, 0
        for i in xrange(1, len(prices)):
        	currMax = max(0, currMax + prices[i] - prices[i - 1])
        	soFarMax = max(currMax, soFarMax)
       	return soFarMax

        # Solution 2 (My solution) :
        """
			use an additional array to store the current profit
			if the (i - 1)th element plus the difference between current buying and selling prices
			makes the profit < 0, reset it back to 0
        """
        res = [0 for _ in xrange(len(prices))]
        for i in xrange(len(prices) - 1):
        	temp = prices[i + 1] - prices[i]
        	res[i] = max(res[i - 1] + temp, 0)
        return max(res)

        
