class Solution(object):
    def zigzag(self, s, n):
        if n == 1 or len(s) < n:
            return s
        res = ["" for _ in xrange(n)]
        index, step = 0, 1
        for c in s:
            res[index] += c
            # if index is 0 (top), start counting downward
            if index == 0:
                step = 1
            # if index is n-1 (bottom), start counting upward
            elif index == n - 1:
                step = -1
            index += step
        return "".join(res)

    def zigzag2(self, s, n):
        if n == 1 or len(s) < n:
            return s

        res = ["" for _ in xrange(n)]
        index = 0
        while index < len(s):
            down = 0
            while down < n and index < len(s):
                res[down] += s[index]
                down += 1
                index += 1
            up = n - 2
            while up >= 1 and index < len(s):
                res[up] += s[index]
                up -= 1
                index += 1
        return "".join(res)
