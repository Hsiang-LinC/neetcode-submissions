class KthLargest:
    '''
        Use a heap structure to store the top K inputs.
        Since only add is allowed, no need to consider removal.

    '''
    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.heap = nums
        self.k = k

        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
    def add(self, val: int) -> int:
        
        if len(self.heap) >= self.k:
            if val > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
        
        return self.heap[0]
        