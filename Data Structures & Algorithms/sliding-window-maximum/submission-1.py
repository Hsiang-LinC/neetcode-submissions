class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
            deque and pop:
            * start from 0 elements, keep the largest element on the left
            * the deque should be in decreasing order
            * append left most element to the result
        '''
        q = collections.deque()
        res = []
        lp, rp = 0, 0

        while rp < len(nums):
            while q and nums[q[-1]] < nums[rp]:
                q.pop()
            q.append(rp)

            if rp - lp + 1 == k:
                res.append(nums[q[0]])
                if q[0] == lp:
                    q.popleft()
                lp += 1
                
            rp += 1
        return res