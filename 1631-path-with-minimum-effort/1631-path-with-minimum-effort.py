class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        R, C = len(heights), len(heights[0])
        q = [(0, 0, 0)]
        visited = set()
        
        while q:
            effort, row, col = heappop(q)
            if (row, col) in visited:
                continue
            visited.add((row, col))
            if (row, col) == (R - 1, C - 1):
                return effort
            
            if row > 0:
                heappush(q, (max(effort, abs(heights[row][col] - heights[row - 1][col])), row - 1, col))
            if col > 0:
                heappush(q, (max(effort, abs(heights[row][col] - heights[row][col - 1])), row, col - 1))
            if row < R - 1:
                heappush(q, (max(effort, abs(heights[row][col] - heights[row + 1][col])), row + 1, col))
            if col < C - 1:
                heappush(q, (max(effort, abs(heights[row][col] - heights[row][col + 1])), row, col + 1))
        