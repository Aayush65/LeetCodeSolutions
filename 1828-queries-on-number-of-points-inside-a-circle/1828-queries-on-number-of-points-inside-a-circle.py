class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        dist = lambda x1, y1, x2, y2: (x1 - x2) ** 2 + (y1 - y2) ** 2
        
        res = []
        for x, y, r in queries:
            count = 0
            for i, j in points:
                count += dist(x, y, i, j) <= r * r
            res.append(count)
        return res