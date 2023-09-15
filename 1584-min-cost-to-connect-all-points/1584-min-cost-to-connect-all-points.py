class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = {i: [] for i in range(n)}
        
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heappush(edges[i], (dist, j))
                heappush(edges[j], (dist, i))
        
        totalCost = 0
        connections = 0
        q = [[0, 0]]
        visited = set()
        
        while q:
            cost, node = heappop(q)
            if node in visited:
                continue
            totalCost += cost
            visited.add(node)
            connections += 1
            
            if connections == n:
                break
            for i in edges[node]:
                heappush(q, i)
            
        return totalCost