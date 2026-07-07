class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # scan through array twice
        # keep one array of products up until current element
        res = [1] * len(nums)
        # update from the second to the end
        for i in range(len(nums)-1):
            res[i+1] = res[i] * nums[i]
        
        # scan from the buttom
        post_prod = 1
        for i in range(len(nums)-1, 0, -1):
            post_prod *= nums[i]
            res[i-1] *= post_prod

        return res