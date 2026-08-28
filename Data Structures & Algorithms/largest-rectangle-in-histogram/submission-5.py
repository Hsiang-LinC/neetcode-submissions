class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
            area = min * nums
        '''
        heights.append(0)
        res = 0
        q = []
        for i in range(len(heights)):
            while q and heights[i] <= heights[q[-1]]:
                qid = q.pop()
                width = i - q[-1] - 1 if len(q) != 0 else i
                res = max(res, width * heights[qid])
            q.append(i)
        return res