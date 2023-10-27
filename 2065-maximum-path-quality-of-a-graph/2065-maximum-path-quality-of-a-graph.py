class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        
        n = len(values)
        nodeMap = {i: [] for i in range(n)}
        for node, nei, time in edges:
            nodeMap[node].append((nei, time))
            nodeMap[nei].append((node, time))
        
        visited = [0] * n
        def backtrack(node: int, spentTime: int) -> int:
            if spentTime > maxTime:
                return 0
            res = 0
            if node == 0:
                res = sum(values[i] for i in range(n) if visited[i])
            for nei, time in nodeMap[node]:
                visited[nei] += 1
                res = max(res, backtrack(nei, time + spentTime))
                visited[nei] -= 1
            return res
                
            
        return max(backtrack(0, 0), values[0])
