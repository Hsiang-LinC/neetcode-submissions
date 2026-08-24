class Solution:
    def trap(self, height: List[int]) -> int:
        '''
            obs:
                1. water at index i depends on the min(max(left), max(right)) - i
                2. one pointer to scan from left, one from right to keep track of current max from both direction.
                3. Could go for 2 scanning from left and right
                4. Better 1 scan linear space sol:
                    1. lp to update maxLeft, rp to update maxRight
                    2. min(maxLeft, maxRight) can be determined on spot
                    3. if lp < rp, then lp < rp <= rightMax[i]
                    4. then we can move smaller pointer right away and get volume
        '''
        lp, rp = 0, len(height) - 1
        res, leftMax, rightMax = 0, 0, 0

        while lp <= rp:
            if leftMax < rightMax:
                res += max(leftMax - height[lp], 0)
                leftMax = max(leftMax, height[lp])
                lp += 1
            else:
                res += max(rightMax - height[rp], 0)
                rightMax = max(rightMax, height[rp])
                rp -= 1
                
        return res