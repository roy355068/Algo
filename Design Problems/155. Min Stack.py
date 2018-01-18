class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        currMin = self.getMin()
        if currMin is None or x < currMin:
            currMin = x
        self.s.append([x, currMin])

    def pop(self):
        """
        :rtype: void
        """
        self.s.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.s[-1][0] if len(self.s) > 0 else None

    def getMin(self):
        """
        :rtype: int
        """
        return self.s[-1][1] if len(self.s) > 0 else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()