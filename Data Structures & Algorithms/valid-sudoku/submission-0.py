class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
            keep 3 hashmaps for col, row, and squares, resp.
            square can be indexed by r/3, c/3
        '''
        hrow = defaultdict(list)
        hcol = defaultdict(list)
        hsqu = defaultdict(list)

        for r in range(len(board)):
            for c in range(len(board[0])):
                a = board[r][c]
                if a == '.':
                    continue
                
                if (a in hrow[r] or a in hcol[c] or a in hsqu[(r // 3, c // 3)]):
                    return False
                else:
                    hrow[r].append(a)
                    hcol[c].append(a)
                    hsqu[(r // 3, c // 3)].append(a)
        
        return True
