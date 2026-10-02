class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edgeMap = {i: set() for i in range(n)}
        for v1, v2 in edges:
            edgeMap[v1].add(v2)
            edgeMap[v2].add(v1)
        
        visited = set()
        comp = 0

        def bfs(node):
            if node in visited:
                return

            nonlocal comp
            comp += 1

            q = collections.deque([node])
            while q:
                p = q.popleft()
                if p in visited:
                    continue
                visited.add(p)

                for nxt in edgeMap[p]:
                    if nxt in visited:
                        continue
                    q.append(nxt)
                    edgeMap[nxt].remove(p)

        for node in range(n):
            bfs(node)

        return comp
        
