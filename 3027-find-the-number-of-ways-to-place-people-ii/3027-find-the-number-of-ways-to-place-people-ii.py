class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        count = 0
        n = len(points)
        points.sort(key = lambda x: [x[0], -x[1]])

        for i in range(n - 1):
            x1, y1 = points[i]
            prev = -float("inf")
            for j in range(i + 1, n):
                x2, y2 = points[j]
                if y2 > y1 or y2 <= prev:
                    continue
                prev = y2
                count += 1
        return count