class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
            ')' must come after '(', the only constraint
            use a counter to track how many ')' allowed
            n - counter '()' remains
        '''
        res = []
        path = []
        left, right = 0, 0

        def dfs(left, right):
            # make sure "(" not less than ")"
            if right > left:
                return

            # terminate when enclosed
            if right == n:
                res.append("".join(path))
                return
            
            # left cap
            if left == n:
                path.append(")")
                dfs(left, right + 1)
                path.pop()
                return
            
            
            # splitting logics
            path.append("(")
            dfs(left + 1, right)
            path.pop()
                
            path.append(")")
            dfs(left, right + 1)
            path.pop()
        
        dfs(0, 0)
        return res
