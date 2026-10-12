class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for i in range(n-1):
            tmp = b
            b += a
            a = tmp
        return b
        
