class Solution:
    def trap(self, height: List[int]) -> int:
        '''
            obs:
                1. water at index i depends on the min(max(left), max(right)) - i
                2. one pointer to scan from left, one from right to keep track of current max from both direction.
        '''
        leftMax, rightMax = [0] * len(height), [0] * len(height)

        curMax = 0
        for i in range(len(height)):
            leftMax[i] = curMax
            curMax = max(curMax, height[i])

        curMax = 0
        res = 0
        for i in range(len(height) - 1, -1, -1):
            rightMax[i] = curMax
            res += max(min(leftMax[i], rightMax[i]) - height[i], 0)
            curMax = max(curMax, height[i])
        
        return res