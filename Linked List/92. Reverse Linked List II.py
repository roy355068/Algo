class Solution(object):
	def reverseBetween(self, head, m, n):
		if m == n:
			return head
		dummy = ListNode(0)
		dummy.next = head
		prev = dummy
		for _ in xrange(m - 1):
			prev = prev.next

		prevNode = None
		curr = prev.next
		for _ in xrange(n - m + 1):
			nextNode = curr.next
			curr.next = prevNode
			prevNode = curr
			curr = nextNode
		prev.next.next = curr					
		prev.next = prevNode
		
		return dummy.next
