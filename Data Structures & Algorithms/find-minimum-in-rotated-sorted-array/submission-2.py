class Solution:
    def findMin(self, nums: List[int]) -> int:
        lp = 0
        rp = len(nums) - 1
        
        while nums[lp] > nums[rp]:
            mid = (lp + rp) // 2
            
            if nums[mid] >= nums[lp]:
                lp = mid + 1
            else:
                rp = mid

        return nums[lp]
