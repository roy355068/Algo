# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    # Find the one celebrity or return -1 for no such person
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        cand = 0
        # if candidate knows someone other than him/herself
        # he/she musn't be the celebrity. On the other hand, a celebrity should
        # be known to anyone else, so the current i would be the new candidate
        for i in xrange(1, n):
            if knows(cand, i):
                cand = i

        # Next we have to check if the candidate is the real celebrity
        for i in xrange(n):
            if cand != i:
                # we should check if our current candidate knows anyone before
                # him/her and make sure everyone knows him/her
                if i < cand and (knows(cand, i) or not knows(i, cand)):
                    return -1
                # A worthnothy point is that the we should only check if the
                # person behind cand knows the candidate since we already know
                # that cand don't know anyone else behind him in the 1st Phase
                elif i > cand and not knows(i, cand):
                    return -1
        return cand
