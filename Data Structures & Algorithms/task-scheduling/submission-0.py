class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
            drain those with most count first
            track valid CDs
            use maxHeap to decide which to choose,
            use queue to track the CDs, time available
        '''
        taskCount = collections.Counter(tasks)
        minHeap = [-v for k, v in taskCount.items()]
        heapq.heapify(minHeap)
        cd = collections.deque()

        t = 0
        while minHeap or cd:
            t += 1
            if cd and cd[0][1] <= t:
                task = cd.popleft()
                heapq.heappush(minHeap, task[0])

            if minHeap:
                task = heapq.heappop(minHeap)
                task += 1
                if task < 0:
                    cd.append((task, t + n + 1))
        
        return t