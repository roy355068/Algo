# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    # Add all element in nestedList from the rear into the stack (self.s)
    # So that the stack could return the very first element when popping
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.s = []
        for i in xrange(len(nestedList) - 1, -1, -1):
            self.s.append(nestedList[i])

    def next(self):
        """
        :rtype: int
        """
        return self.s.pop().getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        # check the first element in the nestedList
        # if the element is an integer, directly return True and let the next() function
        # to do the popping and data extracting
        # else if the current element is an Integer List, unpack it
        # by calling the getList() function and append all the element in the list from
        # the back into the stack (same reason as the initial nestedList)
        while self.s:
            curr = self.s[-1]
            if curr.isInteger():
                return True
            self.s.pop()
            for i in xrange(len(curr.getList()) - 1, -1, -1):
                self.s.append(curr.getList()[i])
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())