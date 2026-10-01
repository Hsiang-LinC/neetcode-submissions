class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        edgeMap = {i:set() for i in range(n)}
        for n1, n2 in edges:
            edgeMap[n1].add(n2)
            edgeMap[n2].add(n1)
        
        visited = set()
        path = set()
        
        def dfs(node):
            if node in visited:
                return False

            path.add(node)
            
            if not edgeMap[node]:
                return True
            
            visited.add(node)
            for nxt in edgeMap[node]:
                edgeMap[nxt].remove(node)
                if not dfs(nxt):
                    return False
            visited.remove(node)
            return True
        
        return dfs(0) and len(path) == n


            