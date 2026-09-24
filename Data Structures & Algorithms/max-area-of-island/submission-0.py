class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
            search through all positions with bfs
            expand queue with neighboring position until no new "1"s
        '''
        Row, Col = len(grid), len(grid[0])
        res = 0
        visited: set(tuple) = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            area = 0
            while q:
                for _ in range(len(q)):
                    row, col = q.popleft()
                    for dr, dc in directions:
                        r = row + dr
                        c = col + dc
                        if not (r < 0 or r >= Row or
                            c < 0 or c >= Col or
                            (r, c) in visited):
                            visited.add((r, c))
                            if grid[r][c] == 1:
                                q.append((r, c))
                                area += 1
            return area

        for r in range(Row):
            for c in range(Col):
                if (r, c) not in visited:
                    visited.add((r, c))
                    if grid[r][c] == 1:
                        area = bfs(r, c) + 1
                        res = max(res, area)
        return res