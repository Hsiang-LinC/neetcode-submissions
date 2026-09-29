class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
            1. crearte adjacency map, where nodes are courses, directed edges are 
            dependencies.
            1.1 move along the edges with dfs
            
            2.  another visited set to check if there're loops
        '''
        # adjacency graph (as map)
        preMap = {i:[] for i in range(numCourses)}
        for crs, prq in prerequisites:
            preMap[crs].append(prq)
        
        # check for recurrance
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if not preMap[crs]:
                return True
            
            visited.add(crs)
            for prq in preMap[crs]:
                if not dfs(prq): return False
            preMap[crs] = []
            visited.remove(crs)
            return True

        for crs in preMap:
            if not dfs(crs): return False
        return True

            