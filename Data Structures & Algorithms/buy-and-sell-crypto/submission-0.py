class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
            
        '''
        curMin = 101
        res = 0
        for p in prices:
            if p > curMin:
                res = max(res, p - curMin)
            else:
                curMin = min(curMin, p)
        return res