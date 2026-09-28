class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
            expand from edge "O"
            else are "X"
        '''
        Row, Col = len(board), len(board[0])
        edge = [(r, 0) for r in range(Row) if board[r][0] == "O"] +\
               [(r, Col-1) for r in range(Row) if board[r][Col-1] == "O"] +\
               [(0, c) for c in range(Col) if board[0][c] == "O"] +\
               [(Row-1, c) for c in range(Col) if board[Row-1][c] == "O"]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set(edge)

        def bfs(starts):
            q = collections.deque(starts)
            
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < Row and
                        0 <= nc < Col and
                        (nr, nc) not in visited and
                        board[nr][nc] == "O"):

                        q.append((nr, nc))
                        visited.add((nr, nc))
            
        bfs(edge)
        for r in range(Row):
            for c in range(Col):
                if (r, c) not in visited and board[r][c] == "O":
                    board[r][c] = "X"
                   