class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = sorted(list(set(i[0] for i in points)))
        maxWidth = 0
        for i in range(1, len(points)):
            maxWidth = max(maxWidth, points[i] - points[i - 1])
        return maxWidth