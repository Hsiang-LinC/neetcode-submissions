class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1 = -heapq.heappop(stones)
            s2 = -heapq.heappop(stones)
            
            if s1 == s2:
                pass
            else:
                heapq.heappush(stones, s2 - s1)

        
        if stones:
            return -1 * stones[0]
        else:
            return 0