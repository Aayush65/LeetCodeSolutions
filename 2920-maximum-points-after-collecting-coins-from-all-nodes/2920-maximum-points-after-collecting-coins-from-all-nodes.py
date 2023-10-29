class Solution:
    def maximumPoints(self, edges: List[List[int]], coins: List[int], k: int) -> int:
        n = len(edges) + 1
        nodeMap = {i: set() for i in range(n)}
        for i, j in edges:
            nodeMap[i].add(j)
            nodeMap[j].add(i)
        
        par = [-1] * n
        q = [0]
        visited = set()
        while q:
            newQ = []
            for node in q:
                visited.add(node)
                for child in nodeMap[node]:
                    if child in visited:
                        continue    
                    par[child] = node
                    nodeMap[child].remove(node)
                    newQ.append(child)
            q = newQ
        
        @cache
        def dp(node: int, halving: int) -> int:
            val = coins[node] // 2 ** halving
            if not nodeMap[node]:
                return max(val - k, val // 2)

            half = val // 2
            kminus = val - k
            for child in nodeMap[node]:
                half += dp(child, min(halving + 1, 13))
                kminus += dp(child, halving)
                
            res = max(half, kminus)                    
            return res
            
        res = dp(0, 0)
        return res