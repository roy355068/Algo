class Solution(object):
    def getImportance(self, employees, id):
        dic = {}
        for e in employees:
            dic[e.id] = e
        return self.helper(dic, id)

    def helper(self, dic, empID):
        root = dic[empID]
        total = root.importance
        for sub in root.subordinates:
            total += self.helper(dic, sub)
        return total
