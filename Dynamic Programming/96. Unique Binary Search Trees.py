class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for _ in xrange(n + 1)]
        dp[0], dp[1] = 1, 1

        for i in xrange(2, n + 1):
            # i : current max nodes upto n
            for j in xrange(1, i + 1):
                # j : the current root up to i

                # G(N) is the actual function we need to derive
                # F(i, N) is using i as root while the total # of nodes is N

                # so we have
                # G(N) = F(1, N) + F(2, N) + F(3, N).... + F(N, N)
                # also F(3, 7) = G(2) * G(4) due to it'll have two subtree with 2 and 4 nodes
                # so we'll have G(N) = G(0) * G(N - 1) + G(1) * G(N - 2) + ... + G(N - 1) * G(0)

                # the left subtree will have j - 1 nodes (because node start from 1 to j - 1)
                # the root is j itself
                # the right subtree will have i - j nodes (nodes start from j + 1 to i)
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[-1]
