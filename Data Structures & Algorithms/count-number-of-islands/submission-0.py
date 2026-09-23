class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Row, Col = len(grid), len(grid[0])
        visited = set()
        islandCount = 0
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in directions:
                        if (Row > (r + dr) >= 0 and
                            Col > (c + dc) >= 0 and 
                            (r + dr, c + dc) not in visited):
                            visited.add((r+dr, c+dc))
                            if grid[r + dr][c + dc] == "1":
                                q.append((r + dr, c + dc))

        for r in range(Row):
            for c in range(Col):
                if not (r < 0 or r >= Row or c < 0 or c >= Col or (r, c) in visited):
                    visited.add((r, c))
                    if grid[r][c] == "1":
                        islandCount += 1
                        bfs(r, c)
        return islandCount
                    