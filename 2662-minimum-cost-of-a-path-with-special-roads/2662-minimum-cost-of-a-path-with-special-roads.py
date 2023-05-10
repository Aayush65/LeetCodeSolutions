class Solution:
    def minimumCost(self, start: List[int], end: List[int], specialRoads: List[List[int]]) -> int:
        h = [(0, start[0], start[1])]
        roadMap = defaultdict(list)
        for sx, sy, ex, ey, c in specialRoads:
            roadMap[(sx, sy)].append((ex, ey, c))
        
        visited = set()
        while h:
            currCost, sx, sy = heappop(h)
            if [sx, sy] == end:
                return currCost
            if (sx, sy) in visited:
                continue
            visited.add((sx, sy))
            heappush(h, (currCost + abs(end[0] - sx) + abs(end[1] - sy), end[0], end[1]))
            for nextX, nextY, cost in roadMap[(sx, sy)]:
                heappush(h, (currCost + cost, nextX, nextY))
            for nextX, nextY in roadMap:
                heappush(h, (currCost + abs(sx - nextX) + abs(sy - nextY), nextX, nextY))