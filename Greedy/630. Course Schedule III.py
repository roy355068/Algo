class Solution(object):
    # courses : List[List[int]]
    # Time is O(N log N) because there will have N adding operation to
    # the heap at the worst case, and each pushing will take logN time for
    # heapification
    # Space is O(N) for the heap
    def scheduleCourse(self, courses):
        start, pq = 0, []
        # sort the array by the ending times
        # to deal with the courses that has the earliest deadlines first
        # so when we consider every courses before a particular course
        # those courses will always ends before the current class's end time
        # no matter taking the course or not
        courses.sort(key = lambda x : x[1])
        for time, end in courses:
            # we need to make sure that the courses we've taken so far
            # has total duration that is smaller than current course's end time
            # so whenever the total duration exceeds the end time, can greedily
            # remove one previous coures with the longest duration to
            # maintain the loop invariant, here can use max heap
            start += time
            heapq.heappush(pq, -time)
            if start > end:
                start += heapq.heappop(pq)
        return len(pq)
        # this solution will always prefer courses with shorter duration
        # than longer ones
