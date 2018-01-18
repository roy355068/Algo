class Solution(object):
    dic = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    def romanToInt(self, s):
        res = 0
        for i, c in enumerate(s):
            currVal = self.dic[c]
            nextVal = self.dic[s[i + 1]] if i < len(s) - 1 else 0
            res += currVal if currVal >= nextVal else -currVal
        return res
