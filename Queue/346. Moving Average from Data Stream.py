from collections import deque
class Solution(object):
    def __init__(self, size):
        # number of current size of the deque
        self.n = 0
        self.size = size
        self.q = deque()
        self.sum = 0.0

    def next(self, val):
        if self.n <= self.size:
            self.n += 1

        self.sum += val
        self.q.append(val)
        # if the size of q exceeds the size limitation, then pop out the
        # left most number from the deque and substract it from the sum
        if q and self.n > self.size:
            self.n = self.size
            self.sum -= self.q.popleft()
        return self.sum / self.n
