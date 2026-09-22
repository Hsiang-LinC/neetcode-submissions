class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        '''
            backtracking to find valid solution
        '''
        diag1 = set()   # r - c
        diag2 = set()   # r + c
        col = set()     # visited columns

        res = []
        path = []

        def dfs(r):
            if r >= n:
                res.append(path.copy())
                return
            
            for c in range(n):
                if c in col or (r - c) in diag1 or (r + c) in diag2:
                    continue
                
                path.append("." * c + "Q" + "." * (n - c - 1))
                col.add(c)
                diag1.add(r - c)
                diag2.add(r + c)

                dfs(r + 1)

                diag1.remove(r - c)
                diag2.remove(r + c)
                col.remove(c)
                path.pop()
        dfs(0)
        return res
                

                

            