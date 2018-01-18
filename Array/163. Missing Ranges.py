class Solution(object):
    def findMissingRanges(self, nums, lower, upper):
        res = []
        for n in nums:
            # use a variable justBelow to keep track of the number that are
            # 1 lower than current number and compare it with the lower pointer
            # and derive the distance from it to decide what content
            # should I put in to the res array
            justBelow = n - 1
            if justBelow == lower:
                res.append(str(lower))
            elif lower < justBelow:
                res.append(str(lower) + "->" + str(justBelow))
            lower = n + 1
            
        # Address missing range between upper bound and the last element in
        # the array
        if lower < upper:
            res.append(str(lower) + "->" + str(upper))
        elif lower == upper:
            res.append(str(upper))
        return res
