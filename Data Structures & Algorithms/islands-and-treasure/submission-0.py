class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
            Dijkstra?
            BFS search on each point to update
            start from sinks
        '''
        Row, Col = len(grid), len(grid[0])
        INF = 2147483647
        q = collections.deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # find sinks and add to the first layer
        for r in range(Row):
            for c in range(Col):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        while q:
            for _ in range(len(q)):
                p = q.popleft()
                for dr, dc in directions:
                    r, c = p[0] + dr, p[1] + dc
                    if (r < 0 or c < 0 or
                        r >= Row or c >= Col or
                        grid[r][c] != INF):
                        continue
                    
                    if grid[r][c] == -1:
                        continue

                    q.append((r, c))
                    grid[r][c] = 1 + grid[p[0]][p[1]]
        return


