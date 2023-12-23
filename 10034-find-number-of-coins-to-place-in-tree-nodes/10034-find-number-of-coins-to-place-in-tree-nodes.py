class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        nodeMap = {i: set() for i in range(n)}
        for i, j in edges:
            nodeMap[i].add(j)
            nodeMap[j].add(i)
            
        coins = [0] * n
    
        visited = set()
        def traverse(node: int) -> None:
            allAllVals = []
            visited.add(node)
            for child in nodeMap[node]:
                if child in visited:
                    continue
                allAllVals.append(traverse(child))

            allVals = []
            for allVal in allAllVals:
                allVals.extend(allVal)
            allVals.append(cost[node])
            allVals.sort()

            if len(allVals) < 3:
                coins[node] = 1
            else:
                maxProd = max(allVals[0] * allVals[1] * allVals[-1], allVals[-3] * allVals[-2] * allVals[-1], 0)
                coins[node] = maxProd
            return allVals

        traverse(0)
        return coins