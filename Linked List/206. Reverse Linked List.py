class Solution(object):
	def reverseList(self, head):
		if not head:
			return None
		prev = None
		curr = head
		while curr:
			nextNode = curr.next
			curr.next = prev
			prev = curr
			curr = nextNode
		return prev