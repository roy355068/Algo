class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        # By definition, k has to be distinct and value of k and t
        # couldn't be negative since they're absolute value
        if k <= 0 or t < 0:
            return False
        # dic is used to do bucket sort
        dic = {}
        # weight is the number that is going to be divided by num in nums
        # to assign bucket for each num
        weight = t + 1
        for i in xrange(len(nums)):
            # index of bucket that the current num belongs to
            index = nums[i] / weight
            # if there's already a element in that bucket, we know
            # that there's definitely a element in array that fulfill the requirement
            if index in dic:
                return True
            # if adjacent bucket has a number that satisfys req,
            # directly return True
            # The buckets that are not adjacent to current won't be possible
            # to have a candidate number due to the bucket size
            elif index - 1 in dic and abs(nums[i] - dic[index - 1]) < weight:
                return True
            elif index + 1 in dic and abs(nums[i] - dic[index + 1]) < weight:
                return True
            # update the bucket.
            # Note that the main difference between this method and the real
            # bucket sort is that each bucket would only have one value
            # at a time in this method, because the collision would result in
            # early termination!
            dic[index] = nums[i]
            # address the requirement of index distance
            if i >= k:
                del dic[nums[i - k] / weight]
        return False
