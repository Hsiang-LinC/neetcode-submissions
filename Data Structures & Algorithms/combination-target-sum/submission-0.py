class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
            repeatable -> contruct set of nums
            subproblem: target = target - nums[i], 
            under contraints target > min(nums)
        '''
        res = []
        path = []
        
        def dfs(i, total):
            '''
                total is sum before this node
                this node we decide if to add nums[i] or not
            '''
            if i == len(nums) or total > target:
                return
            
            if total == target:
                res.append(path.copy())
                return
            
            path.append(nums[i])
            dfs(i, total + nums[i])
            path.pop()
            dfs(i + 1, total)
        
        dfs(0, 0)
        return res