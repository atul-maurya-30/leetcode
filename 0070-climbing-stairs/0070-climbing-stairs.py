class Solution:
    def climbStairs(self, n: int) -> int:
        # we use the concept of tabulation (bottom-up) approach
        # so for that we use the code as

        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1

        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[-1]