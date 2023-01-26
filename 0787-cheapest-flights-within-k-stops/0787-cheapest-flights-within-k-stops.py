class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        nodeMap = {i:[] for i in range(n)}
        for a, b, c in flights:
            nodeMap[a].append((b, c))

        queue = [(src, 0)]
        minCost = float("inf")
        stop = 0
        visited = set()
        while queue and stop < k + 2:
            nextStops = []
            stop += 1
            for currStop, currCost in queue:
                if (currStop, currCost) in visited:
                    continue
                if currStop == dst:
                    minCost = min(minCost, currCost)
                    continue
                for nextStop, nextCost in nodeMap[currStop]:
                    if currCost + nextCost > minCost:
                        continue
                    nextStops.append((nextStop, currCost + nextCost))
                visited.add((currStop, currCost))
            queue = nextStops
        return minCost if minCost != float("inf") else -1