class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [None] * (n+1)
        dp[1] = 1
        if n >= 2:
            dp[2] = 2

        if n > 2:
            for index in range(3, n+1):
                dp[index] = dp[index - 1] + dp[index - 2] 

        return dp[n]