class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
           for a given substring, split at every possible point
           use pass slices -> O(n) time and space complexity
           use l & r pointer -> O(n) time and O(1) space complexity
        '''
        res = []
        path = []

        def dfs(i):
            if i >= len(s):
                res.append(path.copy())
                return
            
            for j in range(i, len(s)):
                if isPalin(s, i, j):
                    path.append(s[i:j+1])
                    dfs(j+1)
                    path.pop()
            
        def isPalin(s, l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        dfs(0)
        return res

