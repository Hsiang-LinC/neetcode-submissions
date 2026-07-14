class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
            OBS: for every new 1, the right side repeat
            ==> DP problem
            base case: dp[0] = 0
            then, dp[2] = 1 + dp[0]; dp[3] = 1 + dp[1]
            dp[4] = 1 + dp[0]; ... dp[7] = 1 + dp[3]
            
            Or: Shifting right, or mod 2, but need to consider odd or even
            if odd --> last bit = 1 --> shift right + 1
            odd or even can be judge by mod 2 or (n & 1)
            dp[i] = 
        '''
        dp = [0] * (n + 1)
        
        for i in range(len(dp)):
            # shift right, add the last 1 if odd
            dp[i] = dp[i >> 1] + (i & 1)
        return dp
            
        