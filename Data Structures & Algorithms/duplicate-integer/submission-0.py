class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use hash map, and scan the array in one sweep
        prev_hash = {}
        for i, num in enumerate(nums):
            if num in prev_hash:
                return True
            else:
                prev_hash[num] = i
        return False