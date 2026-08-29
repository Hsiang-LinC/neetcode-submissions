class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
            binary search for O(logn) time complexity
        '''
        lp, rp = 0, len(nums) - 1
        while lp <= rp:
            mid = (lp + rp) // 2
            if nums[mid] < target:
                lp = mid + 1
            elif nums[mid] > target:
                rp = mid - 1
            else:
                return mid
        return -1