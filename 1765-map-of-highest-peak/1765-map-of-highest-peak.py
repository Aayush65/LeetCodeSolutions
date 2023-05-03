class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m = len(isWater)
        n = len(isWater[0])
        
        q = deque([])
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    q.append((i, j, 0))
            
        heightMap = [[float("inf")] * n for i in range(m)]
        while q:
            x, y, height = q.popleft()
            if x == m or x == -1 or y == n or y == -1:
                continue
            if heightMap[x][y] <= height:
                continue
            heightMap[x][y] = min(heightMap[x][y], height)
            q.append((x + 1, y, height + 1))
            q.append((x, y - 1, height + 1))
            q.append((x - 1, y, height + 1))
            q.append((x, y + 1, height + 1))

        return heightMap