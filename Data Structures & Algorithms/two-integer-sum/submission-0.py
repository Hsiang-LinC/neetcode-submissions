class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # genius way: hash map
        # track the substracted remaining

        num_dict = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff not in num_dict:
                num_dict[num] = i
            else:
                return [num_dict[diff], i]