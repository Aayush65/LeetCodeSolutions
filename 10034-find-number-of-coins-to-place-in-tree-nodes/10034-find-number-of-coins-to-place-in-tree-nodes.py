class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        nodeMap = {i: set() for i in range(n)}
        for i, j in edges:
            nodeMap[i].add(j)
            nodeMap[j].add(i)
            
        coins = [1] * n
    
        visited = set()
        def dfs(node: int) -> None:
            allVals = [cost[node]]
            visited.add(node)
            for child in nodeMap[node]:
                if child in visited:
                    continue
                allVals.extend(dfs(child))

            allVals.sort()
            if len(allVals) > 2:
                allPos = allVals[-3] * allVals[-2] * allVals[-1]
                twoNegOnePos = allVals[0] * allVals[1] * allVals[-1]
                maxProd = max(allPos, twoNegOnePos, 0)
                coins[node] = maxProd
            return allVals

        dfs(0)
        return coins