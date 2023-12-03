class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        def timeTaken(c1: list[int], c2: list[int]) -> int:
            x1, y1 = c1
            x2, y2 = c2
            return max(abs(x1 - x2), abs(y1 - y2))
            
        time = 0
        for i in range(1, len(points)):
            time += timeTaken(points[i], points[i - 1])
        return time