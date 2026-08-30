class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp, rp = 0, len(nums) - 1
        while lp < rp:
            m = (lp + rp) // 2
            if nums[lp] > nums[m]:
                if nums[m] <= target <= nums[rp]:
                    lp = m
                else:
                    rp = m - 1
            else:
                if nums[lp] <= target <= nums[m]:
                    rp = m
                else:
                    lp = m + 1
        return lp if nums[lp] == target else -1

            