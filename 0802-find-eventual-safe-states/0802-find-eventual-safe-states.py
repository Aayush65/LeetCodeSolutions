class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        state = [None]* n
        visited = set()

        def dfs(node: int) -> bool:
            if state[node] != None:
                return state[node]
            if node in visited:
                return False
            res = True
            visited.add(node)
            for i in graph[node]:
                if not dfs(i):
                    res = False
                    break
            visited.remove(node)
            state[node] = res
            return res
        
        for i in range(n):
            dfs(i)
        return [i for i in range(n) if state[i]]