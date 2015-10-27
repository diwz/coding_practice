# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1]*3
        for i in range(2, n+1):
            dp[i % 3] = dp[(i - 1) % 3] + dp[(i - 2) % 3]

        return dp[n % 3]
