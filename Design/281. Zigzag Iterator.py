from collections import deque
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.data = deque([(len(v), iter(v)) for v in (v1, v2) if v])


    def next(self):
        """
        :rtype: int
        """
        length, curr = self.data.popleft()
        if length > 1:
            self.data.append((length - 1, curr))
        return curr.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.data

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
