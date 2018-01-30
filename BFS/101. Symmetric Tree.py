import collections
class Solution(object):
	def isSymmetric(self, root):
		# BFS. push the root twice into queue, then push symmetrical nodes 
		# of the parent into queue (t1.left with t2.right, t1.right with t2.left)
        
        q = collections.deque()
        q.append(root)
        q.append(root)
        while q:
            temp1 = q.popleft()
            temp2 = q.popleft()
            # if temp1 and temp2 are both null, continue traversal
            if not temp1 and not temp2:
                continue
            # if only one of the two nodes is null, then return False
            if not temp1 or not temp2:
                return False
            # if the vals are not identical, return False
            if temp1.val != temp2.val:
                return False
            # push symmetrical nodes into queue
            q.append(temp1.left)
            q.append(temp2.right)
            q.append(temp1.right)
            q.append(temp2.left)
        return True

	def isSymmetric(self, root):
		return self.dfs(root, root)

	def dfs(self, node1, node2):
		if not node1 or not node2:
			return node1 == node2
		elif node1.val != node2.val:
			return False
		return self.dfs(node1.left, node2.right) and self.dfs(node1.right, node2.left)