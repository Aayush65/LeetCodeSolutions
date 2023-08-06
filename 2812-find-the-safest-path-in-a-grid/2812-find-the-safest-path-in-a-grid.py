class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        theives = deque([])
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    theives.append((i, j, 0))
        
        isValid = lambda x, y: -1 < x < n and -1 < y < n
        
        visited = set()
        while theives:
            x, y, safeness = theives.popleft()
            if (x, y) in visited or not isValid(x, y):
                continue
            grid[x][y] = safeness
            visited.add((x, y))
            theives.append((x + 1, y, safeness + 1))
            theives.append((x, y + 1, safeness + 1))
            theives.append((x - 1, y, safeness + 1))
            theives.append((x, y - 1, safeness + 1))           
                
        q = [(-grid[0][0], 0, 0)]
        visited = {}
        maxSafety = 0
        while q:
            safeness, x, y = heappop(q)
            safeness *= -1
            if not isValid(x, y):
                continue
            safeness = min(safeness, grid[x][y])
            if (x, y) in visited and visited[(x, y)] >= safeness:
                continue
            visited[(x, y)] = safeness
            if (x, y) == (n - 1, n - 1):
                maxSafety = max(maxSafety, safeness)
                continue
            heappush(q, (-safeness, x + 1, y))
            heappush(q, (-safeness, x, y + 1))
            heappush(q, (-safeness, x - 1, y))
            heappush(q, (-safeness, x, y - 1))
        return maxSafety

            