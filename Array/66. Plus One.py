class Solution(object):
    def plusOne(self, digits):
        for i in xrange(len(digits) - 1, -1, -1):
            # if exists one single digit that is smaller than nine
            # meaning it doesn't need to carry over on that digit
            # so add one to it and return

            # else means the digit needs to carry over
            # so set it to zero and let the next iteration add one to
            # the next digit
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
