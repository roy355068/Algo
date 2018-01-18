from collections import deque
class Solution(object):
    # do it in-place.
    # Iterative level-order traversal
    # O(N) for time complexity because need to visit every node once
    # O(N) for space complexity because of the queue size
    def connect(self, root):
        if not root:
            return
        dq = deque()
        dq.append(root)
        while dq:
            length = len(dq)
            for i in xrange(length):
                curr = dq.popleft()
                if i != length - 1:
                    curr.next = dq[0]
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)

    # Recursive DFS traversal
    # O(N) for both time and space, space is results from recursion stack
    def connect(self, root):
        if not root:
            return
        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

    # Iterative traversal using two additional pointers
    # O(N) for time complexity while space complexity is only O(1)
    def connect(self, root):
        if not root:
            return
        leftmost, curr = root, None
        while leftmost.left:
            curr = leftmost
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            leftmost = leftmost.left
