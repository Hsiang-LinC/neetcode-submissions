class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        Row, Col = len(board), len(board[0])
        def search(i, j, n):
            if n == len(word):
                return True
            
            if (i >= Row or i < 0 or
                j >= Col or j < 0 or
                board[i][j] != word[n] or
                (i, j) in path):
                return False
            
            path.add((i, j))
            res = (search(i, j + 1, n + 1) or
                   search(i, j - 1, n + 1) or 
                   search(i + 1, j, n + 1) or 
                   search(i - 1, j, n + 1))
            path.remove((i, j))
            return res
        
        for r in range(Row):
            for c in range(Col):
                if search(r, c, 0):
                    return True
        return False
                