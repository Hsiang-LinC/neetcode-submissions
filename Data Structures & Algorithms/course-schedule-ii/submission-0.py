class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range(numCourses)}
        for crs, prq in prerequisites:
            preMap[crs].append(prq)
        
        visiting, visited = set(), set()
        res = []
        
        
        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            
            visited.add(crs)
            visiting.add(crs)

            for prq in preMap[crs]:

                if not dfs(prq):
                    return False
                
            visiting.remove(crs)
            res.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return res