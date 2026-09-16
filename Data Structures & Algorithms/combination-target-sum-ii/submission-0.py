class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
            combination w/o duplicate
        '''
        res = []
        path = []
        skipped = set()

        def dfs(i, total):
            
            if total == target:
                res.append(path.copy())
                return
            if total > target or i >= len(candidates):
                return
            if candidates[i] in skipped:
                dfs(i + 1, total)
                return
            
            path.append(candidates[i])
            dfs(i+1, total + candidates[i])
            path.pop()

            skipped.add(candidates[i])
            dfs(i+1, total)
            skipped.remove(candidates[i])

        dfs(0, 0)
        return res