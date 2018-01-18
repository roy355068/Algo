# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
from collections import *

class Solution(object):

    # Naive way to do this is new the RandomListNode object when we
    # traverse down the linked list
    # O(N) time complexity for 1-pass traversal and O(1) space complexity
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        dummy = RandomListNode(-1)
        curr = dummy

        while head:
            curr.next = RandomListNode(head.label)
            curr = curr.next
            if head.random:
                curr.random = RandomListNode(head.random.label)
            head = head.next

        return dummy.next

    # A better way to do this is using a HashMap to store all the node
    # that had showed up in the traversal so that we don't have to create
    # a lot of redundant nodes

    def copyRandomList(self, head):
        if not head:
            return None
        dic = {}
        dummy = RandomListNode(-1)
        curr = dummy

        while head:

            if head not in dic:
                dic[head] = RandomListNode(head.label)
            curr.next = dic[head]
            curr = curr.next
            # only handle the case that the random pointer is not null
            if head.random:
                # put the node into dictionary for lookup
                if head.random not in dic:
                    dic[head.random] = RandomListNode(head.random.label)
                curr.random = dic[head.random]

            head = head.next
        return dummy.next

    # A space-optimized solution is to duplicate the nodes and
    # put the duplicated node right after each original node
    # Can achieve O(1) space complexity (if exclude the memory for return value)
    # but need 3 pass of O(N) time complexity
    def copyRandomList(self, head):
        if not head:
            return None
        curr, next = head, None
        # Copy all of the "next" pointer into the duplicated nodes
        while curr:
            next = curr.next
            copied = RandomListNode(curr.label)
            curr.next = copied
            copied.next = next
            curr = next

        curr = head

        # Copy all of the "random" pointer into the duplicated nodes
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # extract the copied nodes and restore the original struture of
        # the original list
        dummy = RandomListNode(0)
        curr, currCopy = head, dummy
        copy = None
        while curr:
            # the next original node
            nextNode = curr.next.next

            copy = curr.next
            currCopy.next = copy
            currCopy = currCopy.next

            curr.next = nextNode
            curr = curr.next
        return dummy.next
