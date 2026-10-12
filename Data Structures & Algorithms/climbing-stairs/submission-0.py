class Solution:
    def climbStairs(self, n: int) -> int:
        '''
            dynamic programming: stateful recursion.
            dp[n] = 1 + dp[n-1] + 1 + dp[n-2]
        '''
        dp = {0: 1, 1: 1}
        
        def dfs(n):
            if n in dp:
                return dp[n]
            dp[n] = dfs(n - 1) + dfs(n - 2)
            return dp[n]

        return dfs(n)