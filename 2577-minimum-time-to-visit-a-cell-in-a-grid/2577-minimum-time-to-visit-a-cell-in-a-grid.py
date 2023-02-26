class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        h = [(0, 0, 0)]
        visited = set()
        while h:
            time, i, j = heappop(h)
            if (i, j) == (m - 1, n - 1):
                return time
            if (i, j) in visited:
                continue
            visited.add((i, j))
            for x, y in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if i + x < 0 or i + x == m or j + y < 0 or j + y == n or (i + x, j + y) in visited:
                    continue
                pingPongTime = 0
                if grid[i + x][j + y] - time > 1 and not (grid[i + x][j + y] - time) % 2:
                    pingPongTime = 1
                heappush(h, (max(time + 1, grid[i + x][j + y] + pingPongTime), i + x, j + y))   
        return -1