class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(remain):
            if not remain:
                res.append(path.copy())
                return
            
            for i, num in enumerate(remain):
                path.append(num)
                dfs(remain[:i] + remain[i + 1:])
                path.pop()
                
        
        dfs(nums)
        return res