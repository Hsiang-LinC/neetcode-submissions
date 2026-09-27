class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
            bfs from sink
        '''
        if not heights:
            return []
        Row, Col = len(heights), len(heights[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def bfs(starts):
            visited = set(starts)
            q = collections.deque(starts)
            while q:
                for _ in range(len(q)):
                    p = q.popleft()
                    for dr, dc in directions:
                        r, c = p[0]+dr, p[1]+dc
                        if not (r < 0 or r >= Row or
                            c < 0 or c >= Col or
                            (r, c) in visited):
                            if heights[r][c] >= heights[p[0]][p[1]]:
                                visited.add((r, c))
                                q.append((r, c))
            return visited
        pac = [(r, 0) for r in range(Row)] + [(0, c) for c in range(Col)]
        atl = [(r, Col - 1) for r in range(Row)] + [(Row - 1, c) for c in range(Col)]
        
        return list(bfs(pac) & bfs(atl))