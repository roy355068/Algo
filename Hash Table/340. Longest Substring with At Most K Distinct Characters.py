class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # Char tables, the test cases would not only contain alphabet
        count = [0 for _ in xrange(256)]
        # start : starting point of the sliding window, used for removing
        #         chars when # of distinct chars exceeds k
        # distinct : keeps track of # of distinct chars in the sliding window
        start, distinct, res = 0, 0, 0

        # end : the end of the sliding window
        for end in xrange(len(s)):
            currEnd = ord(s[end])
            # if the count of current char is 0, meaning it's a distinct
            # char, increment variable distinct by 1
            if count[currEnd] == 0:
                distinct += 1
            count[currEnd] += 1

            if distinct <= k:
                res = max(res, end - start + 1)

            # when the # of distinct char exceeds k, start shrinking the
            # window by moving start pointer forward.
            # if if there's a zero after removing char, then we can decrement
            # the number of distinct char in the window
            while distinct > k:
                removing = ord(s[start])
                count[removing] -= 1
                if count[removing] == 0:
                    distinct -= 1
                # Shrink the window
                start += 1
        return res
