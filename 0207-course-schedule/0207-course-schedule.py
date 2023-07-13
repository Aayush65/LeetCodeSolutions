class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodeMap = {i: [] for i in range(numCourses)}
        for i, j in prerequisites:
            nodeMap[i].append(j)
        
        visited = set()

        def dfs(node: int) -> bool:
            if node in visited:
                return False
            if not nodeMap[node]:
                return True
            
            visited.add(node)
            for i in nodeMap[node]:
                if not dfs(i):
                    return False
            visited.remove(node)
            nodeMap[node] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True