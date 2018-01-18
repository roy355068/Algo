from collections import deque
class Solution(object):
    # do it in-place.
    # Iterative level-order traversal
    # O(N) for time complexity because need to visit every node once
    # O(N) for space complexity because of the queue size

    # The first solution is the same as the one in 116.
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

    # The O(1) space solution is trickier than previous questions since
    # the tree might not be complete so it has the possibility to lose some
    # nodes in the levels

    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return
        nextHead, nextCursor, curr = None, None, root
        # in outer loop I want to move curr pointer from one layer to the next layer
        while curr:
            # in inner loop I'll move the curr pointer from left to right in the
            # same layer to set up the next pointer for children for each node
            while curr:
                if curr.left:
                    # if no nextCursor, meaning the next layer is a brand new level that
                    # I haven't seen before, so label the head of next level
                    if not nextCursor:
                        nextHead = curr.left
                    # else, attach the node to the next pointer of the cursor for following traversal
                    else:
                        nextCursor.next = curr.left
                    # move the cursor to the "next" node in the next level
                    nextCursor = curr.left

                # All the same stuff in right child
                if curr.right:
                    if not nextCursor:
                        nextHead = curr.right
                    else:
                        nextCursor.next = curr.right
                    nextCursor = curr.right
                # move the curr pointer in current level
                curr = curr.next
            # place the curr pointer to the head of next level and reset
            # the nextHead and nextCursor to None for next iteration
            curr = nextHead
            nextHead, nextCursor = None, None
