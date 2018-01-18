# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        head = self.head.next
        res = self.head.val
        index = 1
        while head:
            # key! 
            # reservoir sampling, replace with the node of "index" with probability of
            # 1 / index => can make sure that the uniform sampling
            if random.randrange(index + 1) == 0:
                res = head.val
            head = head.next
            index += 1
        return res


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()