class MedianFinder:
    '''
        use 2 heap stack of same size, or at most differ in 1 element count
        one is larger than the other
        small heap -> maxHeap (can have 1 more element)
        large heap -> min Heap 
        if not equal size -> -maxHeap[0]
        else -> (minHeap[0] - maxHeap[0] ) / 2
    '''
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # add num to one heap
        if len(self.small) == 0 or num < -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        
        # rebalance the heaps
        if len(self.large) > len(self.small):
            n = heapq.heappop(self.large)
            heapq.heappush(self.small, -n)
        if len(self.large) < len(self.small) - 1:
            n = heapq.heappop(self.small)
            heapq.heappush(self.large, -n)
            

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return -self.small[0]
        