class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while nums[l] > nums[r]:
            m = (l + r) // 2
            if nums[l] > nums[m]:
                r = m
            else:
                l = m + 1
        return nums[l]