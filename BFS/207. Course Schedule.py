from collections import *
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in xrange(numCourses)]
        # the degree of in-coming courses
        inDegreee = [0 for _ in xrange(numCourses)]
        # q is the queus for node-visiting in BFS
        # count is taking record of how many nodes that has been visited
        q = deque()
        count = 0

        for p in prerequisites:
            inDegreee[p[0]] += 1
            graph[p[1]].append(p[0])

        # start the BFS from the nodes that have no
        # in-coming edge
        for i in xrange(len(inDegreee)):
            if inDegreee[i] == 0:
                q.append(i)
                count += 1
        # if there's cycle in the graph, the count will never be possible
        # to reach numCourses because we cannot take every courses in the graph
        while q:
            curr = q.popleft()
            for course in graph[curr]:
                inDegreee[course] -= 1
                if inDegreee[course] == 0:
                    q.append(course)
                    count += 1
        return True if count == numCourses else False
