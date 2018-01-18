"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
from collections import *

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        res = 0
        if not employees:
            return res

        q = deque()
        empIdMap = {}
        for e in employees:
            empIdMap[e.id] = e

        q.append(empIdMap[id])

        while q:
            curr = q.popleft()
            res += curr.importance
            for sub in curr.subordinates:
                q.append(empIdMap[sub])

        return res
