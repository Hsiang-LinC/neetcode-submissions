class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minK, maxK = 1, max(piles)

        while minK < maxK:
            midK = (minK + maxK) // 2
            hSum = sum((pile + midK - 1) // midK for pile in piles)

            if hSum > h:          # invalid：速度太慢
                minK = midK + 1
            else:                 # valid：midK 可能就是最小答案
                maxK = midK

        return minK