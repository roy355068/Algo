# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        prev, slow, fast = None, head, head
        """
        prev : the tail node of the left part of the linked list
        fast : the tail node of the right part of the linked list
                it'll move twice as fast as slow pointer
        slow : the middle node of the whole linked list.
                In order to build a balanced tree, we need to find the middle
                node and split the whole linked list into halves
        """
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        """
        if prev exists, meaning that there's a tail in the left linked list.
        Break the linked list by setting the tail's next node a None.
        And then use the left and right parts to construct left and right
        subtrees

        if there's no prev exists, meaning that there's no more nodes in the
        left subtree, set the head to None and use the head to construct
        the subtree
        """
        if prev:
            prev.next = None
        else:
            head = None
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root


    def sortedListToBSTWithHelperFunction(self, head):
        if not head:
            return None
        return self.helper(head, None)
    def helper(self, head, tail):
        if head == tail:
            return None
        slow, fast = head, head
        while fast != tail and fast.next != tail:
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        root.left = self.helper(head, slow)
        root.right = self.helper(slow.next, tail)
        return root
