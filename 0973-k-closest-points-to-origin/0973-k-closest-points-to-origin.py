class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []
        for x, y in points:
            dist.append((x**2 + y **2, [x, y]))
        dist.sort()
        res = []
        for i in range(k):
            res.append(dist[i][1])
        return res