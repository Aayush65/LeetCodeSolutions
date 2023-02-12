class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        nodeMap = {i: set() for i in range(len(roads) + 1)}
        for i, j in roads:
            nodeMap[i].add(j)
            nodeMap[j].add(i)
        
        fuel = 0
        def dfs(node: int) -> int:
            cars = 1
            for i in nodeMap[node]:
                nodeMap[i].remove(node)
                cars += dfs(i)
            nonlocal fuel
            fuel += ceil(cars / seats)
            return cars

        for i in nodeMap[0]:
            nodeMap[i].remove(0)
            dfs(i)
        return fuel
