class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
            Union Find Algo.
            Find: the root of each node. If not, add by comparing Rank.
            Rank: the number of child nodes. Start with 1 (itself).
            Union: Check if 2 nodes share the same root.
        '''
        rank = [1] * (len(edges) + 1)
        parent = [i for i in range(len(edges) + 1)]

        def find(v):
            if v != parent[v]:
                parent[v] = find(parent[v])
            return parent[v]

        def union(v1, v2):
            '''
                2 points add together
                if already same parent -> cycle
                else update their parents
            '''
            p1, p2 = find(v1), find(v2)
            if p1 == p2:
                return False
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]

            return True
        
        for v1, v2 in edges:
            if not union(v1, v2):
                return [v1, v2]