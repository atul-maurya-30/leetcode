class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n<2):
            return n
        dp=[0,1,1]
        for i in range(3,n+1):
            next_t=dp[0]+dp[1]+dp[2]
            dp[0],dp[1],dp[2]=dp[1],dp[2],next_t
        return dp[2]
        