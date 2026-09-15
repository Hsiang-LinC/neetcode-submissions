class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        def dfs(prev: list, include: bool, i: int):
            if i >= len(nums):
                return
            if include:
                prev = prev + [nums[i]]
                res.append(prev)
            dfs(prev, True, i + 1)
            dfs(prev, False, i + 1)
        
        dfs([], True, 0)
        dfs([], False, 0)

        return res