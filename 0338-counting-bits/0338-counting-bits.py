class Solution(object):
    def countBits(self, n):
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i // 2] + (i % 2)

        return dp