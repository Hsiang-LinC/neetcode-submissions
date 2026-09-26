class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
            bfs from the rotten
            check when q in empty, if there are 1 remaining
        '''
        def check(grid):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return False
            return True
        
        q = collections.deque()
        Row, Col = len(grid), len(grid[0])

        for r in range(Row):
            for c in range(Col):
                if grid[r][c] == 2:
                    q.append((r, c))
        
        res = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            for _ in range(len(q)):
                p = q.popleft()
                for dr, dc in directions:
                    r, c = p[0] + dr, p[1] + dc
                    if (r < 0 or c < 0 or
                        r >= Row or c >= Col or
                        grid[r][c] != 1):
                        continue
                    q.append((r, c))
                    grid[r][c] = 2
            if q:
                res += 1
        
        return res if check(grid) else -1


