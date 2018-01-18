class Solution(object):
    def removeInvalidParentheses(self, s):
        res = []
        self.remove(res, s, 0, 0, ["(" , ")"])
        return res
    # lastI : starting point of parentheses validity evaluation. Can reduce
    #         repetitive checking of valid prefix

    # lastJ : CRUCIAL!!! In order to prevent duplicated result, we must record
    #         the position of last removed excess parentheses

    def remove(self, res, s, lastI, lastJ, par):
        # stack variable is used to check the validity of the prefix chars in the string
        stack = 0
        for i in xrange(lastI, len(s)):
            stack += (s[i] == par[0]) - (s[i] == par[1])
            # if the parentheses pairs are not matched...
            if stack < 0:
                for j in xrange(lastJ, i + 1):
                    # check if the "right" parentheses is the first char,
                    # or there's no duplicate right in front of it to
                    # avoid generating duplicates
                    if s[j] == par[1] and (j == lastJ or s[j - 1] != par[1]):
                        # by removing char at jth position, the recursion
                        # actually shrunk the string and make the i & j pointers
                        # "increment" by one in the new string,
                        # so that the program won't consider the chars
                        # that has been evaluated
                        self.remove(res, s[:j] +s[j+1:], i, j, par)
                # return is crucial. It only allows the subroutine
                # to check the reversed string after the process from
                # one side is completed
                return

        reverse = s[::-1]
        # if the process from left to right is finished, do it from right
        # to left and exchange the left/right parentheses ordering
        # to remove excess "left" parentheses
        if par[0] == "(":
            self.remove(res, reverse, 0, 0, [")", "("])
        # if the process from right to left is also finished,
        # append the twice-reversed (hence now is not reversed) result into res
        else:
            res.append(reverse)
