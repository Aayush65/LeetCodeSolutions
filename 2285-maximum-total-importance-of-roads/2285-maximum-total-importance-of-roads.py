class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        nodeMap = {i: [] for i in range(n)}
        for i, j in roads:
            nodeMap[i].append(j)
            nodeMap[j].append(i)
        
        maxCost = 0
        cities = sorted(nodeMap.keys(), key = lambda x: len(nodeMap[x]))
        for city, i in zip(cities, range(1, n + 1)):
            maxCost += i * len(nodeMap[city])
        return maxCost