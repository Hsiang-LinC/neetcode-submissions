class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Scan through the list
        # Track largest subarray sum, start from the first num
        # If accu. sum so far < 0, start at next (why add a neg)
        # Always compare to largest (in case all neg numbers)
        larg = nums[0]
        accu = 0
        for i in range(len(nums)):
            accu += nums[i]
            if accu > larg:
                larg = accu
            if accu < 0:
                accu = 0
        return larg