class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp, rp = 0, len(heights) - 1
        res = 0
        while lp < rp:
            res = max(res, (rp - lp) * min(heights[lp], heights[rp]))
            if heights[lp] > heights[rp]:
                rp -= 1
            else:
                lp += 1
        return res
                