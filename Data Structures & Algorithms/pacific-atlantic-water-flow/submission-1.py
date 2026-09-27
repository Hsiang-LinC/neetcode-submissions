class Solution:    
    def pacificAtlantic(self, heights):
        if not heights:
            return []

        rows, cols = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(starts):
            visited = set(starts)
            q = collections.deque(starts)

            while q:
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (0 <= nr < rows and 0 <= nc < cols
                            and (nr, nc) not in visited
                            and heights[nr][nc] >= heights[r][c]):
                        visited.add((nr, nc))
                        q.append((nr, nc))

            return visited

        pacific = [(r, 0) for r in range(rows)] + [(0, c) for c in range(cols)]
        atlantic = [(r, cols - 1) for r in range(rows)] + [(rows - 1, c) for c in range(cols)]

        return list(bfs(pacific) & bfs(atlantic))