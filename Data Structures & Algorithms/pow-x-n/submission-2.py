class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x^n = (x^2)^(n/2) = ((x^2)^2)^(n/4) = ...
        # keep divide n by 2 until n/2 = 1 or n = 2
        # if odd, take floor n // 2
        '''
            10^23 = 10 ^ 22 * 10
            = (10^11)^2 * 10
            = (((10^5)^2) * 10)^2 * 10
            = ((((10^2)^2 * 10)^2 * 10)^2 *10)^2 * 10
            = ...(10^1)...
            = ...(10^0 * 10)
        '''
        # use recursion
        if x == 0:
            return 0
        if n == 0:
            return 1
        elif n == -1:
            return 1/x
        else:
            if abs(n) % 2 == 1:
                p = self.myPow(x, n // 2)
                return p * p * x
            else:
                p = self.myPow(x, n // 2)
                return p * p