class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        res = []
        S = S.replace("-", "").upper()
        if len(S) % K != 0:
            res.append(S[:len(S) % K])
        i = len(S) % K
        while i < len(S):
            res.append(S[i : i + K])
            i += K
        return "-".join(res)
