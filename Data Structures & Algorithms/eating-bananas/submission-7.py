'''
You are given an integer array piles where piles[i] is the number of bananas in the ith pile. You are also given an integer h, which represents the number of hours you have to eat all the bananas.
You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.
Return the minimum integer k such that you can eat all the bananas within h hours.
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
            brute-force: try from 1 until contraints is turn to matching
            binary-search for logn
            max = max(piles), min = 1
        '''
        maxK = max(piles)
        minK = 1
        
        while minK < maxK:
            midK = (minK + maxK) // 2
            hSum = 0
            for i in range(len(piles)):
                hSum += piles[i] // midK + 1 if piles[i] % midK != 0 else piles[i] // midK
            if hSum > h:
                minK = midK + 1  
            else:
                maxK = midK

        return minK
            