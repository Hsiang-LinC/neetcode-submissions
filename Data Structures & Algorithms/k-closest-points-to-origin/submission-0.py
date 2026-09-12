class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            d = x ** 2 + y ** 2
            minHeap.append([d, x, y])
        
        heapq.heapify(minHeap)
        
        res = []
        for _ in range(k):
            p = heapq.heappop(minHeap)
            res.append([p[1], p[2]])

        return res