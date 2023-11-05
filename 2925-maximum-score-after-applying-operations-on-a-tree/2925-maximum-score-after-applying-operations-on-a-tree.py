class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        n = len(values)
        nodeMap = {i: set() for i in range(n)}
        for i, j in edges:
            nodeMap[i].add(j)
            nodeMap[j].add(i)
        
        row = [0]
        while row:
            newRow = []
            for node in row:
                for child in nodeMap[node]:
                    newRow.append(child)
                    nodeMap[child].remove(node)
            row = newRow
        
        total = sum(values)
        
        @cache
        def dp(node: int) -> int:
            res = 0
            for child in nodeMap[node]:
                res += dp(child)
            return min(res, values[node]) if res else values[node]
        
        return total - dp(0)